import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt

# read in the csv file as a pandas dataframe
data = pd.read_csv('Metro_zhvi_uc_sfrcondo_tier_0.33_0.67_sm_sa_month.csv', 
                   skiprows=[1])

# drop cities with missing data
data = data.dropna()

# split the city names and state abbreviations
data[['RegionName', 'State']] = data['RegionName'].str.split(', ', expand=True)

# extract the list of city names from the desired column
city_names = data['RegionName'].tolist()

# read in the shapefiles
states = gpd.read_file("States_shapefile/States_shapefile.shp")
cities = gpd.read_file("USA_Major_Cities/USA_Major_Cities.shp")

# filter the cities shapefile to only include the cities in the list of city names
cities_to_plot = cities[cities['NAME'].isin(city_names)]

# filter out Alaska and Hawaii if necessary
if "AK" not in list(cities_to_plot["ST"]):
    states = states.drop(1)
if "HI" not in list(cities_to_plot["ST"]):
    states = states.drop(11)

# plot the cities and the state boundaries
ax = states.plot(color='white', edgecolor='black', linewidth=0.5)
cities_to_plot.plot(ax=ax, color='red', markersize=.5)

# show the plot
plt.show()
