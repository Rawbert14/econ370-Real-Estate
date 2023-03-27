import pickle
import pandas as pd

# open the file for reading
with open('macro_housing_data_no_cpi', 'rb') as f:
    # deserialize the data and load it back into a dictionary
    loaded_data = pickle.load(f)

for key, df in loaded_data.items():
    if key[1] == 'housing prices':
        df['date'] = pd.to_datetime(df['date']).dt.date
        df['date'] = df['date'] + pd.Timedelta(days=1)
    else:
        df['date'] = pd.to_datetime(df['date']).dt.date

# Get the unique city names and state abbreviations
cities = list(set([key[0] for key in loaded_data.keys()]))

# Initialize an empty dictionary to store the merged DataFrames for each city
merged_time_series = {}

# Loop through the unique city names and state abbreviations
for city_key in cities:
    # Get the housing prices DataFrame for the current city
    df_housing = loaded_data[(city_key, "housing prices")]

    # Initialize the merged DataFrame with the housing prices DataFrame
    merged_df = df_housing

    # Loop through all DataFrames in the dictionary, and merge them if they belong to the current city
    for key, df in loaded_data.items():
        if key[0] == city_key and key[1] != "housing prices":
            merged_df = merged_df.merge(df, on="date", how="left", suffixes=("", f"_{key[1]}"))

    # Set the merged DataFrame's index to the 'Date' column
    merged_df.set_index("date", inplace=True)

    # Add the merged DataFrame to the merged_dfs dictionary
    merged_time_series[city_key] = merged_df\

# save time series data
with open('merged_time_series', 'wb') as f:
    # serialize the dictionary and write it to the file
    pickle.dump(merged_time_series, f)
