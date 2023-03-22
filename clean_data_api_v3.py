
import pandas as pd
import zipfile
import requests
from io import BytesIO
import time
from tqdm import tqdm
import pickle

api_key = 'b2534a6482828132c3baa9e6ae2231c0'  # replace with your FRED API key

# read in housing data as dataframe and drop unnecessary data
housing_url = 'https://files.zillowstatic.com/research/public_csvs/zhvi/Metro_zhvi_uc_sfrcondo_tier_0.33_0.67_sm_sa_month.csv'
data = pd.read_csv(housing_url, skiprows=[1]).dropna()

# split city names and state abbreviations
data[['RegionName', 'State']] = data['RegionName'].str.split(', ', expand=True)

# read in city/county data and drop unnecessary data
cities_url = 'https://simplemaps.com/static/data/us-cities/1.76/basic/simplemaps_uscities_basicv1.76.zip'
response = requests.get(cities_url)
cities_file = BytesIO(response.content)
with zipfile.ZipFile(cities_file, 'r') as zip_file:
    counties = zip_file.extract('uscities.csv')
counties = pd.read_csv(counties)
counties = counties[['city', 'state_id', 'state_name', 'county_name']]

# merge data
data = pd.merge(data, counties, 
                left_on=['RegionName', 'StateName'], 
                right_on=['city', 'state_id'], 
                how='left')

# extract the list of city names from the desired column
cities = data['RegionName'].tolist()
states = data['StateName'].tolist()
counties = data['county_name'].tolist()
state_names = data['state_name'].tolist()

macro_factors = ['Per Capita Personal Income', 'Unemployment Rate', 'Total Gross Domestic Product', 'Resident Population', 'Consumer Price Index for All Urban Consumers: All Items', 'Combined Violent and Property Crime', 'State Tax Collections: T01 Property Taxes']

# create empty dictionary and list to store the time series and errors
series_dict = {}
no_results = []

city_index = 0

# loop over each city and macroeconomic factor
for city in tqdm(cities, desc='Processing cities'):
    state = states[city_index]
    county = counties[city_index]
    state_name = state_names[city_index]
    
    # construct the API request URL
    for factor in macro_factors:
        if factor == 'Per Capita Personal Income' or factor == 'Unemployment Rate' or factor == 'Total Gross Domestic Product' or factor == 'Resident Population' or factor == 'Consumer Price Index for All Urban Consumers: All Items':
            url = f'https://api.stlouisfed.org/fred/series/search?api_key={api_key}&search_text={factor} {city} (MSA)&file_type=json'
        elif factor == 'Combined Violent and Property Crime':
            url = f'https://api.stlouisfed.org/fred/series/search?api_key={api_key}&search_text={factor} {county} county&file_type=json'
        elif factor == 'State Tax Collections: T01 Property Taxes':
            url = f'https://api.stlouisfed.org/fred/series/search?api_key={api_key}&search_text={factor} {state} &file_type=json'
        retry = True
        backoff_time = 1
        while retry:
        
            # make the API request and retrieve the JSON response
            response = requests.get(url)
            if response.status_code == 200:
                json_data = response.json()
                
                # check if there are any results
                if json_data['count'] == 0:
                    no_results.append(f'No results found for {factor} and {city}')
                    # Set to exit the while retry loop
                    retry = False
                    continue

                for i in pd.Series(range(min(json_data['count'], 1000))):
                    
                    # get the desired result
                    series_id = json_data['seriess'][i]['id']
                    series_title = json_data['seriess'][i]['title']
                    
                    found = False
                    # check if the title is correct
                    if factor == 'Per Capita Personal Income' or factor == 'Unemployment Rate' or factor == 'Total Gross Domestic Product' or factor == 'Resident Population':
                        substrings = [f'{factor}', f'{city}', f'{state}', '(MSA)']
                        if all(substring in series_title 
                               for substring in substrings):
                            found = True
                            break
                    elif factor == 'Consumer Price Index for All Urban Consumers: All Items':
                        substrings = [f'{factor}', f'{city}', f'{state}', 'All Items', 'SA)']
                        if all(substring in series_title for substring in substrings):
                            found = True
                            break
                    elif factor == 'Combined Violent and Property Crime':
                        substrings = [f'{factor}', f'{county}', f'{state}', 'County']
                        if all(substring in series_title for substring in substrings):
                            found = True
                            break
                    elif factor == 'State Tax Collections: T01 Property Taxes':
                        substrings = [f'{factor}', f'{state_name}', 'State']
                        if all(substring in series_title for substring in substrings):
                            found = True
                            break
                
                if not found:
                    no_results.append(f'Series not found for {factor} and {city}')
                    # set to exit the while retry loop
                    retry = False
                    continue
                
                # construct the API request URL and make the request
                url = f"https://api.stlouisfed.org/fred/series/observations?series_id={series_id}&api_key={api_key}&file_type=json"
                response = requests.get(url)
                    
                if response.status_code == 200:
                    # retrieive the JSON response
                    data = response.json()
                    
                    # create a dictionary of the data
                    data_dict = {"date": [observation["date"] for observation in data["observations"]],
                                 "value": [observation["value"] for observation in data["observations"]]}
                    
                    # convert the data dictionary to a table
                    df = pd.DataFrame(data_dict)
                    
                    # store the table in a dictionary
                    series_dict[(city, state, factor)] = df
                else:
                    no_results.append(f'Connection error for {factor} and {city}')
                
                # set to exit the while retry loop
                retry = False
            
            else:
                if backoff_time > 512: # maximum of 64 seconds
                    retry = False
                else:
                    backoff_time *= 2  # exponential backoff
                    print(f"Retrying in {backoff_time} seconds...")
                    time.sleep(backoff_time)
                
    # adds one to the city_index to change the state
    city_index += 1

# save time series data
with open('clean_macro_city_data', 'wb') as f:
    # serialize the dictionary and write it to the file
    pickle.dump(series_dict, f)

# save no_results data
with open("clean_no_results.txt", "w") as f:
    for item in no_results:
        f.write(str(item) + "\n")

