# econ370-Real-Estate

The `clean_data_api_v3.py` file is used to pull all of the macro factor data from FRED. It does not require any data or external files to run. It outputs and saves the `clean_macro_city_data` file, which is a dictionary of all of the time series found, and the `clean_no_results` file, which is a list of the variables that were not found.
The `manipulate_and_clean_data.py` file requires the `clean_macro_city_data` file, in order to clean the data and manipulate it into usable dataframes. It outputs and saves the `merged_time_series` file, which is a dictionary of all of the dataframes.
The `clean_map_v4.py` file requires the `merged_time_series` file to create maps of the cities used in the analysis.
The `visualization.py` file creates the data visualizations using the `merged_time_series` file.
The `aic_model.py` file uses the `merged_time_series` file to create the ARDL model. It outputs and saves the fitted ARDL model in the `ardl_model.pkl` file.
The `city_forecasting_v2.py` file uses the `ardl_model.pkl` file to predict the housing prices using the ARDL model, and plot the results.
The `Case Study.py` file uses the `merged_time_series` file to get growth rates for each city.
