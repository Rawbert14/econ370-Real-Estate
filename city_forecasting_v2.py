import pickle
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def load_data():
    # open the file for reading
    with open('merged_time_series', 'rb') as f:
        # deserialize the data and load it back into a dictionary
        merged_time_series = pickle.load(f)
    return merged_time_series
    
def load_model():
    # Open the model
    with open('ardl_model.pkl', 'rb') as f:
        # deserialize the data and load it back into a dictionary
        model = pickle.load(f)
    
    return model

def prep_in_sample_data(merged_time_series):
    in_sample_dict = {}
    # Define the start and end dates
    start_date = '2004-01-01'
    end_date = '2020-12-31'
    
    for key, df in merged_time_series.items():
        filtered_df = df.copy()
        filtered_df = df[(df.index >= start_date) & (df.index <= end_date)]
        filtered_df.fillna(method='ffill', inplace=True)  # Forward-fill
        filtered_df.fillna(method='bfill', inplace=True)  # Backward-fill
        filtered_df = filtered_df.asfreq('MS')  # Set the frequency to Month Start
        in_sample_dict[key] = filtered_df
    
    return in_sample_dict

def prep_oos_data(merged_time_series, end_date):
    oos_dict = {}
    # Define the start and end dates
    start_date = '2021-01-01'
    end_date = end_date
    
    for key, df in merged_time_series.items():
        filtered_df = df.copy()
        filtered_df.fillna(method='ffill', inplace=True)  # Forward-fill
        filtered_df.fillna(method='bfill', inplace=True)  # Backward-fill
        filtered_df = filtered_df[(filtered_df.index >= start_date) & (filtered_df.index <= end_date)]
        filtered_df = filtered_df.asfreq('MS')  # Set the frequency to Month Start
        oos_dict[key] = filtered_df
    
    return oos_dict

def prep_forecasting_data(merged_time_series, start_date):
    forecasting_dict = {}

    start_date = start_date
    end_date = '2026-01-01'
    for key, df in merged_time_series.items():
        new_index = pd.date_range(start=df.index.min(), end=end_date, freq='MS')
        filtered_df = df.reindex(new_index, method='ffill')
        filtered_df.fillna(method='ffill', inplace=True)  # Forward-fill
        filtered_df = filtered_df[(filtered_df.index > start_date) & (filtered_df.index <= end_date)]
        forecasting_dict[key] = filtered_df
    
    return forecasting_dict

def get_average_df(df_dict):
    average_df = pd.DataFrame(data=0,
                              index=next(iter(df_dict.values())).index,
                              columns=next(iter(df_dict.values())).columns)
    
    # Iterate through the DataFrames in the dictionary and sum their values element-wise
    for df in df_dict.values():
        average_df += df
    
    # Divide by the number of DataFrames to get the average
    average_df /= len(df_dict)
    
    return average_df

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
    gdp = data.loc[index - pd.DateOffset(months=1) : index, 'value_gdp'].values[::-1]
    population = data.loc[index - pd.DateOffset(months=1) : index, 'value_population'].values[::-1]
    crime = data.loc[index - pd.DateOffset(months=1) : index, 'value_crime'].values[::-1]
    cpi = data.loc[index - pd.DateOffset(months=2) : index, 'value_cpi'].values[::-1]
    interest = data.loc[index - pd.DateOffset(months=3) : index, 'value_interest'].values[::-1]

    # Concatenate all values into a single array
    current_and_lagged_values = np.concatenate(([1], housing, income, unemployment, gdp, population, crime, cpi, interest))
    
    return current_and_lagged_values

def compute_forecast(index, data, coefficients, forecasts):
    # Extract current values and lagged values based on index
    current_and_lagged_values = extract_current_and_lagged_values_forecasts(index, data, forecasts)
    
    # Compute the dot product of the coefficients and the current and lagged values
    return np.dot(coefficients, current_and_lagged_values)

def extract_current_and_lagged_values_forecasts(index, data, forecasts):

    # Extract the current and lagged values for the variables
    housing = forecasts[-3:]
    income = data.loc[index - pd.DateOffset(months=3) : index, 'value_income'].values[::-1]
    unemployment = data.loc[index - pd.DateOffset(months=1) : index, 'value_unemployment'].values[::-1]
    gdp = data.loc[index - pd.DateOffset(months=1) : index, 'value_gdp'].values[::-1]
    population = data.loc[index - pd.DateOffset(months=1) : index, 'value_population'].values[::-1]
    crime = data.loc[index - pd.DateOffset(months=1) : index, 'value_crime'].values[::-1]
    cpi = data.loc[index - pd.DateOffset(months=2) : index, 'value_cpi'].values[::-1]
    interest = data.loc[index - pd.DateOffset(months=3) : index, 'value_interest'].values[::-1]

    # Concatenate all values into a single array
    current_and_lagged_values = np.concatenate(([1], housing, income, unemployment, gdp, population, crime, cpi, interest))
    
    return current_and_lagged_values

def plot_results(data, predictions, city):
    # Plot the first DataFrame
    ax = data.plot(y='value', label='actual', color='blue')

    # Plot the second DataFrame on the same axis
    predictions.plot(y='0', label='prediction', color='red', ax=ax)
    
    # Customize the plot
    plt.xlabel('Time')
    plt.ylabel('Housing Value ($)')
    plt.title(f'{city} Housing Market')
    plt.legend()

    # Show the plot
    plt.show()
    
def plot_forecasts(predictions, city):
    # Plot the second DataFrame on the same axis
    predictions.plot(y='0', label='prediction', color='red')
    
    # Customize the plot
    plt.xlabel('Time')
    plt.ylabel('Housing Value ($)')
    plt.title(f'{city} Housing Market')
    plt.legend()

    # Show the plot
    plt.show()

def plot_all_results(data, predictions, city, forecast_start):
    # Plot the first DataFrame
    ax = data.plot(y='value', label='actual', color='blue')

    # Plot the second DataFrame on the same axis
    predictions.plot(y='0', label='prediction', color='red', ax=ax)
    
    # Seperate periods
    oos_start = '2021-01-01'
    forecast_start = forecast_start
    plt.axvline(x=oos_start, linestyle='--', color='gray')
    plt.axvline(x=forecast_start, linestyle='--', color='gray')

    # Customize the plot
    plt.xlabel('Time')
    plt.ylabel('Housing Value ($)')
    plt.title(f'{city} Housing Market')
    plt.legend()

    # Show the plot
    plt.show()
    
def main():
    cities_of_interest = ['Average', 'Fayetteville, NC', 'Salt Lake City, UT', 'Omaha, NE'] # In format: 'City Name, State Abbreviation'
    merged_time_series = load_data()
    model = load_model()
    forecast_start = merged_time_series[cities_of_interest[1]].index[-1]
    in_sample_dict = prep_in_sample_data(merged_time_series)
    oos_dict = prep_oos_data(merged_time_series, forecast_start)
    forecast_dict = prep_forecasting_data(merged_time_series, forecast_start)
    in_sample_average = get_average_df(in_sample_dict)
    oos_average = get_average_df(oos_dict)
    forecast_average = get_average_df(forecast_dict)
    
    for city in cities_of_interest:
        # In-Sample Predictions
        if city == 'Average':
            in_sample_data = in_sample_average
        else:
            in_sample_data = in_sample_dict[city]
        in_sample_predictions = []

        for index in in_sample_data.index[3:]:
            in_sample_prediction = compute_prediction(index, in_sample_data, model.params)
            in_sample_predictions.append(in_sample_prediction)

        in_sample_predictions = pd.Series(in_sample_predictions, index=in_sample_data.index[3:])
        plot_results(in_sample_data, in_sample_predictions, city)
        
        # Out-of-Sample Predictions
        if city == 'Average':
            oos_data = oos_average
        else:
            oos_data = oos_dict[city]
        oos_predictions = []

        for index in oos_data.index[3:]:
            oos_prediction = compute_prediction(index, oos_data, model.params)
            oos_predictions.append(oos_prediction)

        oos_predictions = pd.Series(oos_predictions, index=oos_data.index[3:])
        plot_results(oos_data, oos_predictions, city)
        
        # Forecasting
        if city == 'Average':
            forecast_data = forecast_average
        else:
            forecast_data = forecast_dict[city]
        initial_housing_value = forecast_data['value'].iloc[0]
        forecasts = [initial_housing_value, initial_housing_value, initial_housing_value]

        for index in forecast_data.index[3:]:
            forecast = compute_forecast(index, forecast_data, model.params, forecasts)
            forecasts.append(forecast)

        forecasts = pd.Series(forecasts, index=forecast_data.index)
        plot_forecasts(forecasts, city)
        
        # Merge all plots
        all_data = pd.concat([in_sample_data, oos_data])
        all_predictions = pd.concat([in_sample_predictions, oos_predictions, forecasts])
        plot_all_results(all_data, all_predictions, city, forecast_start)


main()