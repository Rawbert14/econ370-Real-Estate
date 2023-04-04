import pickle
from statsmodels.tsa.ardl import ardl_select_order

# open the file for reading
with open('merged_time_series', 'rb') as f:
    # deserialize the data and load it back into a dictionary
    merged_time_series = pickle.load(f)

filled_dict = {}

for key, df in merged_time_series.items():
    filled_df = df.copy()
    filled_df.fillna(method='ffill', inplace=True)  # Forward-fill
    filled_df.fillna(method='bfill', inplace=True)  # Backward-fill
    filled_df = filled_df.asfreq('MS')  # Set the frequency to Month Start
    filled_dict[key] = filled_df

criteria = {}

df = filled_dict['Akron, OH']

ardl_model_housing = ardl_select_order(
    df.value, 3, df[['value_income', 'value_unemployment', 'value_gdp', 'value_population', 'value_crime', 'value_tax', 'value_cpi']], 3, ic="aic", trend="c"
)

criteria['Akron, OH'] = ardl_model_housing

test = criteria['Akron, OH']
optimal_order = test.model.ardl_order
print(f'The optimal order is: {optimal_order}')

