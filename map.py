import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt

# read in the csv file as a pandas dataframe
data = pd.read_csv('zillow_housing.csv')

# extract the list of city names from the desired column
city_names = data['RegionName'].tolist()

# read in the shapefiles
states = gpd.read_file("States_shapefile/States_shapefile.shp")
cities = gpd.read_file("USA_Major_Cities/USA_Major_Cities.shp")

# filter the cities shapefile to only include the cities in the list of city names
cities_to_plot = cities[cities['NAME'].isin(city_names)]

# plot the cities and the state boundaries
ax = states.plot(color='white', edgecolor='black', linewidth=0.5)
cities_to_plot.plot(ax=ax, color='red', markersize=.5)

# show the plot
plt.show()
