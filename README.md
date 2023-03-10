# econ370-Real-Estate

## Pull Data
### Necessary Files
The [Metro_zhvi_uc_sfrcondo_tier_0.33_0.67_sm_sa_month.csv](Metro_zhvi_uc_sfrcondo_tier_0.33_0.67_sm_sa_month.csv) file contains housing price data over time for a number of cities; it is also accessible at https://www.zillow.com/research/data/.  
The zipfile [simplemaps_uscities_basicv1.76.zip](simplemaps_uscities_basicv1.76.zip) contains a file that has county names for every city; it is also accessible here at https://simplemaps.com/data/us-cities.
### Code
The [clean_data_api.py](clean_data_api.py) code pulls macro data from FRED for every city which has complete housing price data.
This data is stored in the [clean_macro_city_data](clean_macro_city_data) dictionary.  
Searches for data which yield no results is stored in the [clean_no_results.txt](clean_no_results.txt) file.

## Combine Macro and Housing Data
### Necessary Files
The [clean_macro_city_data](clean_macro_city_data) dictionary contains macro data from FRED for every city which has complete housing price data; it is also created with the [clean_data_api.py](clean_data_api.py) code.
The [Metro_zhvi_uc_sfrcondo_tier_0.33_0.67_sm_sa_month.csv](Metro_zhvi_uc_sfrcondo_tier_0.33_0.67_sm_sa_month.csv) file contains housing price data over time for a number of cities; it is also accessible at https://www.zillow.com/research/data/.
### Code
The [combine_macro_and_housing_data.py](combine_macro_and_housing_data.py) code combines the housing price data for every city which has complete housing price data with the macro data pulled from FRED.
This data is stored in the [macro_and_housing_data](macro_and_housing_data) dictionary.

## Open Dictionaries
### Necessary Files
The [macro_and_housing_data](macro_and_housing_data) dictionary contains the housing price data for every city which has complete housing price data and the macro data pulled from FRED; it is also created with the [combine_macro_and_housing_data.py](combine_macro_and_housing_data.py) code.
The [clean_no_results.txt](clean_no_results.txt) file contains a list of searches of FRED data which yielded no results; it is also created with the [clean_data_api.py](clean_data_api.py) code.
### Code
The [open_dictionary.py](open_dictionary.py) code opens the [macro_and_housing_data](macro_and_housing_data) dictionary and [clean_no_results.txt](clean_no_results.txt) file in python.  
The code can be adapted to open other dictionaries, such as the [clean_macro_city_data](clean_macro_city_data) dictionary, by changing the file name in the "open()" function.

## Track Variables
### Necessary Files
The [macro_and_housing_data](macro_and_housing_data) dictionary contains the housing price data for every city which has complete housing price data and the macro data pulled from FRED; it is also created with the [combine_macro_and_housing_data.py](combine_macro_and_housing_data.py) code.
### Code
The [variable_tracker.py](variable_tracker.py) code creates a dataframe which shows which variables were found for each city.
This data is stored in the [variable_tracke.csv](variable_tracker.csv) file.
