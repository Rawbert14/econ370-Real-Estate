
#%% IMPORT
import pickle
import pandas as pd

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
        renamed_variable = 'uemployment'
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

housing_and_macro_data = renamed_macro_city_data

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

macro_housing_data_no_cpi = {}

for key, value in housing_and_macro_data.items():
    if 'cpi' not in key:
        macro_housing_data_no_cpi[key] = value

'''
# save time series data
with open('macro_housing_data_no_cpi', 'wb') as f:
    # serialize the dictionary and write it to the file
    pickle.dump(macro_housing_data_no_cpi, f)
'''

#%% MERGE TIME SERIES

'''
# open the file for reading
with open('macro_housing_data_no_cpi', 'rb') as f:
    # deserialize the data and load it back into a dictionary
    macro_housing_data_no_cpi = pickle.load(f)
'''

for key, df in macro_housing_data_no_cpi.items():
    if key[1] == 'housing':
        df['date'] = pd.to_datetime(df['date'])
        df['date'] = df['date'] + pd.Timedelta(days=1)
    else:
        df['date'] = pd.to_datetime(df['date'])

# Get the unique city names and state abbreviations
cities = list(set([key[0] for key in macro_housing_data_no_cpi.keys()]))

# Initialize an empty dictionary to store the merged DataFrames for each city
merged_time_series = {}

# Loop through the unique city names and state abbreviations
for city_key in cities:
    # Get the housing prices DataFrame for the current city
    df_housing = macro_housing_data_no_cpi[(city_key, 'housing')]

    # Initialize the merged DataFrame with the housing prices DataFrame
    merged_df = df_housing

    # Loop through all DataFrames in the dictionary, and merge them if they belong to the current city
    for key, df in macro_housing_data_no_cpi.items():
        if key[0] == city_key and key[1] != 'housing':
            merged_df = merged_df.merge(df, on='date', how='left', suffixes=('', f'_{key[1]}'))

    # Set the merged DataFrame's index to the 'Date' column
    merged_df.set_index('date', inplace=True)
    
    # Prep for interpolation
    for col in merged_df.columns:
        merged_df[col] = pd.to_numeric(merged_df[col], errors='coerce')
        
    # Interpolate the data
    df_monthly = merged_df.resample('MS').interpolate()

    # Add the merged DataFrame to the merged_dfs dictionary
    merged_time_series[city_key] = df_monthly

# Drop cities without all variables
merged_time_series = {key: df for key, df in merged_time_series.items() if df.shape[1] == 7}


# save time series data
with open('merged_time_series', 'wb') as f:
    # serialize the dictionary and write it to the file
    pickle.dump(merged_time_series, f)

