import pickle
import pandas as pd


# open the file for reading
with open('merged_time_series', 'rb') as f:
    # deserialize the data and load it back into a dictionary
    merged_time_series = pickle.load(f)


# change to whatever specific city you want

specific_city = merged_time_series['Salt Lake City, UT'] 

gr_list=[]


for city, df in merged_time_series.items():
    
    gr = (( df.iloc[-1]["value"] - df.iloc[0]["value"] ) / df.iloc[0]["value"])
    gr_list.append(gr)
    
