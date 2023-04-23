import pickle
import pandas as pd
import numpy as np
from statsmodels.tsa.ardl import ardl_select_order
import matplotlib.pyplot as plt

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


# Get model selection
ardl_selection_results = ardl_select_order(
    all_cities['value'], 3, 
    all_cities[['value_income', 'value_unemployment', 'value_gdp', 'value_population', 'value_crime', 'value_tax', 'value_cpi', 'value_interest']], 3, 
    ic="aic", trend="c"
)

# Save the results
with open('ardl_selection_results.pkl', 'wb') as f:
    pickle.dump(ardl_selection_results, f)

optimal_order = ardl_selection_results.model.ardl_order
print(f'The optimal order is: {optimal_order}')

ardl_model = ardl_selection_results.model.fit()
print(ardl_model.summary())

# Save the model
with open('ardl_model.pkl', 'wb') as f:
    pickle.dump(ardl_model, f)
