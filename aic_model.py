import pickle
import pandas as pd
from statsmodels.tsa.ardl import ardl_select_order

# open the file for reading
with open('merged_time_series', 'rb') as f:
    # deserialize the data and load it back into a dictionary
    merged_time_series = pickle.load(f)

cities_dict = {}
# Define the start and end dates
start_date = '2004-01-01'
end_date = '2021-12-31'

for key, df in merged_time_series.items():
    filtered_df = df.copy()
    filtered_df = df[(df.index >= start_date) & (df.index <= end_date)]
    filtered_df.fillna(method='ffill', inplace=True)  # Forward-fill
    filtered_df.fillna(method='bfill', inplace=True)  # Backward-fill
    filtered_df = filtered_df.asfreq('MS')  # Set the frequency to Month Start
    cities_dict[key] = filtered_df

# Assuming your DataFrames are stored in a dictionary called 'dataframes_dict'
dataframes = list(cities_dict.values())

# Concatenate the DataFrames vertically
all_cities = pd.concat(dataframes)

ardl_model_housing = ardl_select_order(
    all_cities['value'], 3, 
    all_cities[['value_income', 'value_unemployment', 'value_gdp', 'value_population', 'value_crime', 'value_tax', 'value_cpi', 'value_interest']], 3, 
    ic="aic", trend="c"
)

# Save the results
with open('ardl_model_housing.pkl', 'wb') as f:
    pickle.dump(ardl_model_housing, f)

dl_lags = ardl_model_housing.dl_lags

optimal_order = ardl_model_housing.model.ardl_order
print(f'The optimal order is: {optimal_order}')

ardl_model = ardl_model_housing.model.fit()
print(ardl_model.summary())

