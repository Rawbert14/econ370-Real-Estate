# econ370-Real-Estate

## Pull Data

The "Metro_zhvi_uc_sfrcondo_tier_0.33_0.67_sm_sa_month" (accessible here: https://www.zillow.com/research/data/) file and a file within the folder "simplemaps_uscities_basicv1.76" (accessible here: https://simplemaps.com/data/us-cities) are used in the "clean_data_api.py" code.

The "clean_macro_city_data" is a python dictionary that contains the time series pulled from FRED using the "clean_data_api.py" code.

The "clean_no_results.txt" is a text file that contains a list of all of the time series searches that failed to yield results.

The "open_dictionary.py" is a python file that contains code to open the "clean_macro_city_data" and "clean_no_results.txt" files in python.
