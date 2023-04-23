import pickle
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def load_and_prep_city_data():
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
    
    return cities_dict

def load_model():
    # Open the model
    with open('ardl_model.pkl', 'rb') as f:
        # deserialize the data and load it back into a dictionary
        model = pickle.load(f)
    
    return model

def compute_prediction(index, data, coefficients):
    # Extract current values and lagged values based on index
    current_and_lagged_values = extract_current_and_lagged_values(index, data)
    
    # Compute the dot product of the coefficients and the current and lagged values
    return np.dot(coefficients, current_and_lagged_values)


def extract_current_and_lagged_values(index, data):

    # Extract the current and lagged values for the variables
    housing = data.loc[index - pd.DateOffset(months=3) : index - pd.DateOffset(1), 'value'].values[::-1]
    income = data.loc[index - pd.DateOffset(months=3) : index, 'value_income'].values[::-1]
    unemployment = data.loc[index - pd.DateOffset(months=1) : index, 'value_unemployment'].values[::-1]
    gdp = data.loc[index - pd.DateOffset(months=3) : index, 'value_gdp'].values[::-1]
    population = data.loc[index - pd.DateOffset(months=1) : index, 'value_population'].values[::-1]
    crime = data.loc[index - pd.DateOffset(months=1) : index, 'value_crime'].values[::-1]
    tax = data.loc[index - pd.DateOffset(months=2) : index, 'value_tax'].values[::-1]
    cpi = data.loc[index - pd.DateOffset(months=3) : index, 'value_cpi'].values[::-1]
    interest = data.loc[index - pd.DateOffset(months=3) : index, 'value_interest'].values[::-1]

    # Concatenate all values into a single array
    current_and_lagged_values = np.concatenate(([1], housing, income, unemployment, gdp, population, crime, tax, cpi, interest))
    
    return current_and_lagged_values

def plot_results(forecasting_data, predictions, city):
    # Plot the first DataFrame
    ax = forecasting_data.plot(y='value', label='actual', color='blue')

    # Plot the second DataFrame on the same axis
    predictions.plot(y='0', label='forecast', color='red', ax=ax)

    # Customize the plot
    plt.xlabel('Time')
    plt.ylabel('Housing Value')
    plt.title(f'{city} Housing Market')
    plt.legend()

    # Show the plot
    plt.show()
    
def main():
    cities_of_interest = ['Fayetteville, NC', 'Salt Lake City, UT', 'Omaha, NE'] # In format: 'City Name, State Abbreviation'
    cities_dict = load_and_prep_city_data()
    model = load_model()
    for city in cities_of_interest:
        forecasting_data = cities_dict[city]
        predictions = []
    
        for index in forecasting_data.index[3:]:
            prediction = compute_prediction(index, forecasting_data, model.params)
            predictions.append(prediction)
    
        predictions = pd.Series(predictions, index=forecasting_data.index[3:])
        plot_results(forecasting_data, predictions, city)

main()