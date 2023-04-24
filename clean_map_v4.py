
#%% IMPORT AND READ IN DATA
import pandas as pd
import geopandas as gpd
import pickle
import matplotlib.pyplot as plt

#%% STAGE 1
# read in housing data as dataframe and drop unecessary data
housing_url = 'https://files.zillowstatic.com/research/public_csvs/zhvi/Metro_zhvi_uc_sfrcondo_tier_0.33_0.67_sm_sa_month.csv'
data = pd.read_csv(housing_url, skiprows=[1])

# get all city names
city_names = data['RegionName'].tolist()

# read in the shapefiles and filter the cities shapefile to only include the cities in the list of city names
states = gpd.read_file('https://services2.arcgis.com/DEoxb4q3EJppiDKC/arcgis/rest/services/States_shapefile/FeatureServer/0/query?outFields=*&where=1%3D1&f=geojson')
cities = gpd.read_file('https://stacks.stanford.edu/file/druid:bx729wr3020/data.zip', compression='zip')
cities['full_name'] = cities['NAME'] + ', ' + cities['STATE']
stage1_cities_to_plot = cities[cities['full_name'].isin(city_names)]

#%% STAGE 2
no_na_data = data.dropna()
no_na_city_names = no_na_data['RegionName'].tolist()
stage2_cities_to_plot = cities[cities['full_name'].isin(no_na_city_names)]



#%% STAGE 3
with open('merged_time_series', 'rb') as f:
    # deserialize the data and load it back into a dictionary
    merged_time_series = pickle.load(f)
dict_cities = list(set([key for key in merged_time_series.keys()]))
stage3_cities_to_plot = cities[cities['full_name'].isin(dict_cities)]

#%% PLOT MAP
all_stages = [stage1_cities_to_plot, stage2_cities_to_plot, stage3_cities_to_plot]
for cities_to_plot in all_stages:
    # create a new figure with three subplots
    fig = plt.figure(figsize=(10, 6), dpi=300)
    ax1 = fig.add_subplot()
    ax2 = fig.add_subplot()
    ax3 = fig.add_subplot()
    
    # set standard parameters
    edgecolor = 'black'
    facecolor = 'lightgrey'
    linewidth = .5
    color = 'red'
    markersize = 5
    
    # plot the US states on the first subplot and the cities on top of the states
    states.plot(ax=ax1, edgecolor=edgecolor, facecolor=facecolor, linewidth=linewidth)
    cities_to_plot.plot(ax=ax1, color=color, markersize=markersize)
    cities_to_plot.plot(ax=ax2, color=color, markersize=markersize)
    cities_to_plot.plot(ax=ax3, color=color, markersize=20)
    
    # set the limits of the first subplot to zoom in on the continental US and remove the axis numbers
    ax1.set_xlim([-130, -64])
    ax1.set_ylim([20, 52])
    ax1.set_xticklabels([])
    ax1.set_yticklabels([])
    ax1.tick_params(length=0, labelsize=0)
    ax1.annotate('Selected Cities for Real Estate Analysis', xy=(-121, 50), fontsize=20, color='black')
    
    # plot Alaska on the second subplot and remove the axis numbers
    states[states['State_Name'] == 'ALASKA'].plot(ax=ax2, edgecolor=edgecolor, facecolor=facecolor, linewidth=linewidth)
    ax2.set_xlim([-182, -125])
    ax2.set_ylim([48, 74])
    ax2.set_xticklabels([])
    ax2.set_yticklabels([])
    ax2.tick_params(length=0, labelsize=0)
    ax2.annotate('Alaska', xy=(-151, 49.5), fontsize=13, color='black')
    
    # Adjust the position of the second subplot
    ax2.set_position([0.1, 0.15, 0.22, 0.22])
    
    # plot Hawaii on the third subplot and remove the axis numbers
    states[states['State_Name'] == 'HAWAII'].plot(ax=ax3, edgecolor=edgecolor, facecolor=facecolor, linewidth=linewidth)
    ax3.set_xlim([-162, -153])
    ax3.set_ylim([18, 23])
    ax3.set_xticklabels([])
    ax3.set_yticklabels([])
    ax3.tick_params(length=0, labelsize=0)
    ax3.annotate('Hawaii', xy=(-161.7, 18.38), fontsize=13, color='black')
    
    # Adjust the position of the third subplot to overlap with the first subplot
    ax3.set_position([0.295, 0.15, 0.14, 0.14])
    
    # save and show the map
    plt.savefig('clean_map.png')
    plt.show()
