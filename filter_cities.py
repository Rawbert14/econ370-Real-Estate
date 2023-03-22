import pandas as pd

variable_tracker = pd.read_csv('variable_tracker.csv')

variable_tracker = variable_tracker.drop(['Consumer Price Index for All Urban Consumers: All Items'], axis=1)

filtered_cities = variable_tracker[(variable_tracker.iloc[:, 1:] == 1).all(axis=1)]

# save variable_tracker to csv
filtered_cities.to_csv('filtered_cities_with_cpi.csv')
