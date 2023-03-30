
#%% IMPORT
import pickle
import pandas as pd
import requests

#%% CHANGE KEY NAMES

# open the file for reading
with open('clean_macro_city_data', 'rb') as f:
    # deserialize the data and load it back into a dictionary
    clean_macro_city_data = pickle.load(f)

renamed_macro_city_data = {}

# rename variables
for key, value in clean_macro_city_data.items():
    city_name, state_abbr, variable = key
    if variable == 'Per Capita Personal Income':
        renamed_variable = 'income'
    elif variable == 'Unemployment Rate':
        renamed_variable = 'unemployment'
    elif variable == 'Total Gross Domestic Product':
        renamed_variable = 'gdp'
    elif variable == 'Resident Population':
        renamed_variable = 'population'
    elif variable == 'Consumer Price Index for All Urban Consumers: All Items':
        renamed_variable = 'cpi'
    elif variable == 'Combined Violent and Property Crime':
        renamed_variable = 'crime'
    elif variable == 'State Tax Collections: T01 Property Taxes':
        renamed_variable = 'tax'
        
    new_key = (f"{city_name}, {state_abbr}", renamed_variable)

    renamed_macro_city_data[new_key] = value

'''
# save combined data
with open('renamed_macro_city_data', 'wb') as f:
    # serialize the dictionary and write it to the file
    pickle.dump(renamed_macro_city_data, f)
'''

#%% COMBINE HOUSING AND MACRO DATA

'''
# open the file for reading
with open('renamed_macro_city_data', 'rb') as f:
    # deserialize the data and load it back into a dictionary
    renamed_macro_city_data = pickle.load(f)
'''

# read in housing data as dataframe and drop unecessary data
housing_url = 'https://files.zillowstatic.com/research/public_csvs/zhvi/Metro_zhvi_uc_sfrcondo_tier_0.33_0.67_sm_sa_month.csv'
data = pd.read_csv(housing_url, skiprows=[1]).dropna()

# split city names and state abbreviations
data[['RegionName', 'State']] = data['RegionName'].str.split(', ', expand=True)

# Initialize combined dictionary
housing_and_macro_data = renamed_macro_city_data.copy()

# iterate over each row in the dataframe
for index, row in data.iterrows():
    # create a new pandas dataframe containing the time series data for that city
    city_name = row['RegionName']
    state_abbr = row['StateName']
    prices = row[5:-1].values.tolist()  # get the housing prices for the city as a list
    df = pd.DataFrame({'date': data.columns[5:-1], 'value': prices})
    housing_and_macro_data[(f"{city_name}, {state_abbr}", 'housing')] = df

'''
# save combined data
with open('housing_and_macro_data', 'wb') as f:
    # serialize the dictionary and write it to the file
    pickle.dump(housing_and_macro_data, f)
'''

#%% TAKE ACCOUNT OF VARIABLES

'''
# open the file for reading
with open('housing_and_macro_data', 'rb') as f:
    # deserialize the data and load it back into a dictionary
    housing_and_macro_data = pickle.load(f)
'''

# Get unique cities and variables
cities = list(set([(key[0]) for key in housing_and_macro_data.keys()]))
variables = list(set([key[1] for key in housing_and_macro_data.keys()]))

# Create dataframe with zeros
variable_tracker = pd.DataFrame(0, index=cities, columns=variables)

# Set values to 1 if variable is present for city
for key, value in housing_and_macro_data.items():
    city, variable = key
    if variable in variables and city in cities:
        variable_tracker.loc[city, variable] = 1

'''
# save variable_tracker to csv
variable_tracker.to_csv('variable_tracker.csv')
'''

#%% DROP CPI Data

'''
# open the file for reading
with open('macro_and_housing_data', 'rb') as f:
    # deserialize the data and load it back into a dictionary
    loaded_data = pickle.load(f)
'''

# Initialize filtered dictionary
macro_housing_data_no_cpi = {}

# Only include non-CPI series
for key, value in housing_and_macro_data.items():
    if 'cpi' not in key:
        macro_housing_data_no_cpi[key] = value

'''
# save time series data
with open('macro_housing_data_no_cpi', 'wb') as f:
    # serialize the dictionary and write it to the file
    pickle.dump(macro_housing_data_no_cpi, f)
'''

#%% Add US CPI and INTEREST RATE DATA FOR EACH CITY

api_key = 'b2534a6482828132c3baa9e6ae2231c0'  # replace with your FRED API key

cpi_id = 'CPIAUCSL'

# construct the API request URL and make the request
url = f"https://api.stlouisfed.org/fred/series/observations?series_id={cpi_id}&api_key={api_key}&file_type=json"
response = requests.get(url)

data = response.json()

# create a dictionary of the data
data_dict = {"date": [observation["date"] for observation in data["observations"]],
             "value": [observation["value"] for observation in data["observations"]]}

# convert the data dictionary to a table
cpi = pd.DataFrame(data_dict)

interest_id = 'FEDFUNDS'

# construct the API request URL and make the request
url = f"https://api.stlouisfed.org/fred/series/observations?series_id={interest_id}&api_key={api_key}&file_type=json"
response = requests.get(url)

data = response.json()

# create a dictionary of the data
data_dict = {"date": [observation["date"] for observation in data["observations"]],
             "value": [observation["value"] for observation in data["observations"]]}

# convert the data dictionary to a table
interest = pd.DataFrame(data_dict)

# Inititalize dictionary for adding cpi data
macro_housing_data_with_cpi_interest = macro_housing_data_no_cpi.copy()

cities = list(set([(key[0]) for key in macro_housing_data_no_cpi.keys()]))

for city in cities:
    macro_housing_data_with_cpi_interest[city, 'cpi'] = cpi.copy()
    macro_housing_data_with_cpi_interest[city, 'interest'] = interest.copy()

'''
# save time series data
with open('macro_housing_data_with_cpi_interest', 'wb') as f:
    # serialize the dictionary and write it to the file
    pickle.dump(macro_housing_data_with_cpi_interest, f)
'''

#%% INTERPOLATE DATA

'''
# open the file for reading
with open('macro_housing_data_with_cpi_interest', 'rb') as f:
    # deserialize the data and load it back into a dictionary
    macro_housing_data_with_cpi_interest = pickle.load(f)
'''

# Initialize new dictionary for interpolated data
interpolated_series = {}

# Reecognize series dates
for key, df in macro_housing_data_with_cpi_interest.items():
    if key[1] == 'housing':
        df['date'] = pd.to_datetime(df['date'])
        df['date'] = df['date'] + pd.Timedelta(days=1)
    else:
        df['date'] = pd.to_datetime(df['date'])
    
    # Set date as index
    df.set_index('date', inplace=True)
    
    # Prep for interpolation
    df['value'] = pd.to_numeric(df['value'], errors='coerce')
    
    # Interpolate the data
    merged_df = df.resample('MS').interpolate()
    
    # Add interpolated data to new dictionary
    interpolated_series[key] = merged_df

# Get the unique city names and state abbreviations
cities = list(set([key[0] for key in interpolated_series.keys()]))

# Initialize an empty dictionary to store the merged DataFrames for each city
merged_time_series = {}

# Loop through the unique city names and state abbreviations
for city_key in cities:
    # Get the housing prices DataFrame for the current city
    df_housing = interpolated_series[(city_key, 'housing')]

    # Initialize the merged DataFrame with the housing prices DataFrame
    merged_df = df_housing

    # Loop through all DataFrames in the dictionary, and merge them if they belong to the current city
    for key, df in interpolated_series.items():
        if key[0] == city_key and key[1] != 'housing':
            merged_df = merged_df.merge(df, on='date', how='left', suffixes=('', f'_{key[1]}'))

    # Add the merged DataFrame to the merged_dfs dictionary
    merged_time_series[city_key] = merged_df

# Drop cities without all variables
merged_time_series = {key: df for key, df in merged_time_series.items() if df.shape[1] == 9}

# save time series data
with open('merged_time_series', 'wb') as f:
    # serialize the dictionary and write it to the file
    pickle.dump(merged_time_series, f)

