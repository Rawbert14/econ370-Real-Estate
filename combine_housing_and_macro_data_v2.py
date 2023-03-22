import pickle
import pandas as pd

# open the file for reading
with open('clean_macro_city_data', 'rb') as f:
    # deserialize the data and load it back into a dictionary
    loaded_data = pickle.load(f)

# read in housing data as dataframe and drop unecessary data
housing_url = 'https://files.zillowstatic.com/research/public_csvs/zhvi/Metro_zhvi_uc_sfrcondo_tier_0.33_0.67_sm_sa_month.csv'
data = pd.read_csv(housing_url, skiprows=[1]).dropna()

# split city names and state abbreviations
data[['RegionName', 'State']] = data['RegionName'].str.split(', ', expand=True)

# iterate over each row in the dataframe
for index, row in data.iterrows():
    # create a new pandas dataframe containing the time series data for that city
    city = row['RegionName']
    state = row['StateName']
    prices = row['2000-01-31':'2023-01-31'].values.tolist()  # get the housing prices for the city as a list
    df = pd.DataFrame({'date': data.columns[5:-1], 'value': prices})
    loaded_data[(city, state, 'housing prices')] = df

# save combined data
with open('macro_and_housing_data', 'wb') as f:
    # serialize the dictionary and write it to the file
    pickle.dump(loaded_data, f)

