import pickle
import pandas as pd

# open the file for reading
with open('macro_and_housing_data', 'rb') as f:
    # deserialize the data and load it back into a dictionary
    data = pickle.load(f)

# Get unique cities and variables
cities = list(set([(key[0], key[1]) for key in data.keys()]))
variables = list(set([key[2] for key in data.keys()]))

# Create dataframe with zeros
variable_tracker = pd.DataFrame(0, index=[f"{city}, {state}" for city, state in cities], columns=variables)

# Set values to 1 if variable is present for city
for key, value in data.items():
    city, state, variable = key
    if variable in variables and (city, state) in cities:
        variable_tracker.loc[f"{city}, {state}", variable] = 1
    
# save variable_tracker to csv
variable_tracker.to_csv('variable_tracker.csv')

# open variable_tracker.csv as a df with the city names as the index
loaded_data = pd.read_csv("variable_tracker.csv", index_col=0)