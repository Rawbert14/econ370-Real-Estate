import pickle

# open the file for reading
with open('macro_and_housing_data', 'rb') as f:
    # deserialize the data and load it back into a dictionary
    loaded_data = pickle.load(f)

macro_housing_data_no_cpi = {}

for key, value in loaded_data.items():
    if 'Consumer Price Index for All Urban Consumers: All Items' in key:
        macro_housing_data_no_cpi[key] = value

# save time series data
with open('macro_housing_data_no_cpi', 'wb') as f:
    # serialize the dictionary and write it to the file
    pickle.dump(macro_housing_data_no_cpi, f)