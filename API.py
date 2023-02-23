
import requests
import pandas as pd
import time
import pickle

api_key = 'b2534a6482828132c3baa9e6ae2231c0'  # Replace with your FRED API key

# read in the csv file as a pandas dataframe
data = pd.read_csv('Metro_zhvi_uc_sfrcondo_tier_0.33_0.67_sm_sa_month.csv', skiprows=[1])
data[['RegionName', 'State']] = data['RegionName'].str.split(', ', expand=True)
counties = pd.read_csv('simplemaps_uscities_basicv1.76/uscities.csv')
counties = counties[['city', 'state_id', 'state_name', 'county_name']]

# merge data
data = pd.merge(data, counties, left_on=['RegionName', 'StateName'], right_on=['city', 'state_id'], how='left')

# extract the list of city names from the desired column
cities = data['RegionName'].tolist()
states = data['StateName'].tolist()
counties = data['county_name'].tolist()
state_names = data['state_name'].tolist()

macro_factors = ['Per Capita Personal Income', 'Unemployment Rate', 'Total Gross Domestic Product', 'Resident Population', 'Combined Violent and Property Crime', 'T01 Property Taxes']

# Initialize an empty dictionary and list to store the time series and errors
series_dict = {}
no_results = []

city_index = 0

# Loop over each city and macroeconomic factor
for city in cities:
    state = states[city_index]
    county = counties[city_index]
    state_name = state_names[city_index]
    
    # to track progress
    print(city)
    for factor in macro_factors:
        if factor == 'Per Capita Personal Income' or 'Unemployment Rate' or 'Total Gross Domestic Product' or 'Resident Population':
            # Construct the API request URL
            url = f'https://api.stlouisfed.org/fred/series/search?api_key={api_key}&search_text={factor} {city} (MSA)&file_type=json'
        elif factor == 'Combined Violent and Property Crime':
            # Construct the API request URL
            url = f'https://api.stlouisfed.org/fred/series/search?api_key={api_key}&search_text={factor} {county} county&file_type=json'
        elif factor == 'T01 Property Taxes':
            # Construct the API request URL
            url = f'https://api.stlouisfed.org/fred/series/search?api_key={api_key}&search_text={factor} {state} &file_type=json'
        retry = True
        backoff_time = 1
        while retry:
        
            # Make the API request and retrieve the JSON response
            response = requests.get(url)
            if response.status_code == 200:
                json_data = response.json()
                
                # Check if there are any results
                if json_data['count'] == 0:
                    no_results.append(f'No results found for {factor} and {city}')
                    # Set to exit the while retry loop
                    retry = False
                    continue

                for i in pd.Series(range(min(json_data['count'], 1000))):
                    
                    # Get the desired result
                    series_id = json_data['seriess'][i]['id']
                    series_title = json_data['seriess'][i]['title']
                    
                    found = False
                    # Check if the title is correct
                    if factor == 'Per Capita Personal Income' or 'Unemployment Rate' or 'Total Gross Domestic Product' or 'Resident Population':
                        substrings = [f'{factor}', f'{city}', f'{state}', '(MSA)']
                        if all(substring in series_title for substring in substrings):
                            found = True
                            break
                    elif factor == 'Combined Violent and Property Crime':
                        substrings = [f'{factor}', f'{county}', f'{state}', 'County']
                        if all(substring in series_title for substring in substrings):
                            found = True
                            break
                    elif factor == 'T01 Property Taxes':
                        substrings = [f'{factor}', f'{state_name}', 'State']
                        if all(substring in series_title for substring in substrings):
                            found = True
                            break
                
                if not found:
                    no_results.append(f'Series not found for {factor} and {city}')
                    # Set to exit the while retry loop
                    retry = False
                    continue
                
                # Construct the API request URL and make the request
                url = f"https://api.stlouisfed.org/fred/series/observations?series_id={series_id}&api_key={api_key}&file_type=json"
                response = requests.get(url)
                    
                if response.status_code == 200:
                    # Retrieive the JSON response
                    data = response.json()
                    
                    # Create a dictionary of the data
                    data_dict = {"date": [observation["date"] for observation in data["observations"]],
                                 "value": [observation["value"] for observation in data["observations"]]}
                    
                    # Convert the data dictionary to a table
                    df = pd.DataFrame(data_dict)
                    
                    # Store the table in a dictionary
                    series_dict[(city, state, factor)] = df
                else:
                    no_results.append(f'Connection error for {factor} and {city}')
                
                # Set to exit the while retry loop
                retry = False
            
            else:
                if backoff_time > 512: # maximum of 64 seconds
                    retry = False
                else:
                    backoff_time *= 2  # exponential backoff
                    print(f"Retrying in {backoff_time} seconds...")
                    time.sleep(backoff_time)
                
    # Adds one to the city_index to change the state
    city_index += 1

# open a file for saving time series data
with open('macro_city_data', 'wb') as f:
    # serialize the dictionary and write it to the file
    pickle.dump(series_dict, f)

# open a file for saving no_results data
with open("no_results.txt", "w") as f:
    for item in no_results:
        f.write(str(item) + "\n")

