north = [
    "Erie, PA", "Binghamton, NY", "Rochester, MN", "Minneapolis, MN", "Fargo, ND",
    "Duluth, MN", "Milwaukee, WI", "Ann Arbor, MI", "Grand Rapids, MI", "Utica, NY",
    "Syracuse, NY", "Buffalo, NY", "Rochester, NY"
]

south = [
    "Miami, FL", "Homosassa Springs, FL", "Orlando, FL", "Tampa, FL", "Gainesville, FL",
    "Port St. Lucie, FL", "Panama City, FL", "Tallahassee, FL", "Daphne, AL", "Cape Coral, FL",
    "North Port, FL", "Punta Gorda, FL", "Ocean City, NJ", "Palm Bay, FL", "Crestview, FL",
    "Sebastian, FL", "Deltona, FL", "The Villages, FL", "Hilton Head Island, SC", "Charleston, SC",
    "Houston, TX", "San Antonio, TX", "Austin, TX", "New Bern, NC", "Mobile, AL",
    "Montgomery, AL", "Tuscaloosa, AL", "Birmingham, AL", "Jackson, TN", "Memphis, TN",
    "Tulsa, OK", "El Paso, TX"
]

west = [
    "San Diego, CA", "Santa Cruz, CA", "Vallejo, CA", "Santa Rosa, CA", "San Luis Obispo, CA",
    "Redding, CA", "Bakersfield, CA", "Modesto, CA", "Santa Maria, CA", "Salinas, CA",
    "Medford, OR", "Fresno, CA", "Stockton, CA", "Sacramento, CA", "Riverside, CA",
    "Oxnard, CA", "Los Angeles, CA", "Napa, CA", "Kahului, HI", "Eugene, OR", "Salem, OR",
    "Portland, OR", "Reno, NV"
]

east = [
    "Baltimore, MD", "Hagerstown, MD", "Atlantic City, NJ", "Vineland, NJ", "Washington, VA",
    "Ithaca, NY", "Albany, NY", "York, PA", "Altoona, PA", "Reading, PA", "Trenton, NJ",
    "Kingston, NY", "California, MD"
]

northwest = [
    "Idaho Falls, ID", "Greeley, CO", "Boulder, CO", "Colorado Springs, CO", "Pine Bluff, AR",
    "Asheville, NC", "Cedar Rapids, IA", "Des Moines, IA", "Pueblo, CO", "Lincoln, NE",
    "Ogden, UT", "Salt Lake City, UT", "Seattle, WA", "Spokane, WA", "Boise, ID",
    "Billings, MT", "Missoula, MT", "Anchorage, AK", "Fairbanks, AK", "Juneau, AK"
]

northeast = [
    "Niles, MI", "Bay City, MI", "Lansing, MI", "Midland, MI", "Cincinnati, OH", "Cleveland, TN",
    "Muskegon, MI", "Toledo, OH", "Detroit, MI",
    "Chicago, IL", "Lafayette, IN", "Akron, OH", "Boston, MA", "Providence, RI",
    "Hartford, CT", "Springfield, MA", "Worcester, MA", "Burlington, VT",
    "Manchester, NH", "Portland, ME"
]

southeast = [
    "Rocky Mount, NC", "Raleigh, NC", "Greenville, SC",
    "Hickory, NC", "Hot Springs, AR", "Monroe, MI", "Greensboro, NC",
    "Bowling Green, KY", "Goldsboro, NC", "Fayetteville, NC",
    "Evansville, IN", "Jonesboro, AR", "Columbus, OH", 
    "Tuscaloosa, AL", "Atlanta, GA", 
    "Jackson, MS", "New Orleans, LA", "Mobile, AL", "Charleston, WV",
    "Fort Smith, AR", "Nashville, TN", "Charlotte, NC", 
    "Orlando, FL", "Tampa, FL", "Miami, FL", "Jacksonville, FL", "Fort Lauderdale, FL",
    "West Palm Beach, FL", "Sarasota, FL", "Fort Myers, FL"
]

southwest = [
    "Omaha, NE", "Danville, IL", "Santa Fe, NM", "El Paso, TX", "Oklahoma City, OK",
    "Tucson, AZ", "Las Vegas, NV", "Riverside, CA",
    "Palm Springs, CA", "San Diego, CA", "Los Angeles, CA", "Santa Barbara, CA",
    "San Francisco, CA", "Oakland, CA", "San Jose, CA", "Sacramento, CA",
    "Bakersfield, CA", "Reno, NV", "Salt Lake City, UT", "Denver, CO",
    "Pueblo, CO",  "Midland, TX",
    "Odessa, TX", "San Angelo, TX", "Dallas, TX",
    "Fort Worth, TX", "Austin, TX", "San Antonio, TX", "Houston, TX",
    "Beaumont, TX", "Port Arthur, TX",  "Lafayette, LA"
]

len(north)+len(south)+len(west)+len(east)+len(southwest)+len(southeast)+len(northeast)+len(northwest)
import pickle
import matplotlib.pyplot as plt
from pandas.plotting import autocorrelation_plot

# open the file for reading
with open('merged_time_series', 'rb') as f:
    # deserialize the data and load it back into a dictionary
    merged_time_series = pickle.load(f)

north_cities = [
    "Erie, PA", "Binghamton, NY", "Rochester, MN", "Minneapolis, MN", "Fargo, ND",
    "Duluth, MN", "Milwaukee, WI", "Ann Arbor, MI", "Grand Rapids, MI", "Utica, NY",
    "Syracuse, NY", "Buffalo, NY", "Rochester, NY"
]

# Create a figure and axis to plot on
fig, ax = plt.subplots(figsize=(12, 6))

# Iterate through the dictionary containing the DataFrames for each city
for city, df in merged_time_series.items():
    if city in north_cities:
        # Plot the housing prices for the current city
        ax.plot(df.index, df['value'], label=city)

# Set the title, xlabel, and ylabel
ax.set_title('Housing Prices for North Cities')
ax.set_xlabel('Date')
ax.set_ylabel('Housing Price')
ax.legend()

# Display the legend and show the plot
plt.show()
plt.savefig('housing_prices_north.png')


# Create a figure and axis to plot on
fig, ax = plt.subplots(figsize=(12, 6))

# Iterate through the dictionary containing the DataFrames for each city
for city, df in merged_time_series.items():
    if city in north_cities:
        # Calculate and plot the autocorrelations of the housing prices for the current city
        autocorrelation_plot(df['value'])

# Set the title, xlabel, and ylabel
ax.set_title('Autocorrelations of Housing Prices for North Cities')
ax.set_xlabel('Lag')
ax.set_ylabel('Autocorrelation')

# Display the legend and show the plot
plt.show()
plt.savefig('autocorrelation_north.png')


# Create a figure and axis to plot on
fig, ax = plt.subplots(figsize=(12, 6))

# Iterate through the dictionary containing the DataFrames for each city
for city, df in merged_time_series.items():
    # Plot the unemployment values for the current city
    if city in north_cities:
      ax.plot(df.index, df['value_unemployment'], label=city)

# Set the title, xlabel, and ylabel
ax.set_title('Unemployment North Cities')
ax.set_xlabel('Date')
ax.set_ylabel('Unemployment Rate')

# Add a legend
ax.legend()

# Display the plot
plt.show()

# Save the plot to a file
#fig.savefig('unemployment.png')


# Create a figure and axis to plot on
fig, ax = plt.subplots(figsize=(12, 6))

# Iterate through the dictionary containing the DataFrames for each city
for city, df in merged_time_series.items():
    # Plot the unemployment values for the current city
    if city in north_cities:
      ax.plot(df.index, df['value_income'], label=city)

# Set the title, xlabel, and ylabel
ax.set_title('Income North Cities')
ax.set_xlabel('Date')
ax.set_ylabel('Income Rate')

# Add a legend
ax.legend()

# Display the plot
plt.show()

# Save the plot to a file
#fig.savefig('unemployment.png')



# Create a figure and axis to plot on
fig, ax = plt.subplots(figsize=(12, 6))

# Iterate through the dictionary containing the DataFrames for each city
for city, df in merged_time_series.items():
    # Plot the unemployment values for the current city
    if city in north_cities:
      ax.plot(df.index, df['value_gdp'], label=city)

# Set the title, xlabel, and ylabel
ax.set_title('GDP North Cities')
ax.set_xlabel('Date')
ax.set_ylabel('GDP Rate')

# Add a legend
ax.legend()

# Display the plot
plt.show()

# Save the plot to a file
#fig.savefig('unemployment.png')



# Create a figure and axis to plot on
fig, ax = plt.subplots(figsize=(12, 6))

# Iterate through the dictionary containing the DataFrames for each city
for city, df in merged_time_series.items():
    # Plot the unemployment values for the current city
    if city in north_cities:
      ax.plot(df.index, df['value_population'], label=city)

# Set the title, xlabel, and ylabel
ax.set_title('Population North Cities')
ax.set_xlabel('Date')
ax.set_ylabel('Population Rate')

# Add a legend
ax.legend()

# Display the plot
plt.show()

# Save the plot to a file
#fig.savefig('unemployment.png')


# Create a figure and axis to plot on
fig, ax = plt.subplots(figsize=(12, 6))

# Iterate through the dictionary containing the DataFrames for each city
for city, df in merged_time_series.items():
    # Plot the unemployment values for the current city
    if city in north_cities:
      ax.plot(df.index, df['value_crime'], label=city)

# Set the title, xlabel, and ylabel
ax.set_title('Crimes North Cities')
ax.set_xlabel('Date')
ax.set_ylabel('Crimes Rate')

# Add a legend
ax.legend()

# Display the plot
plt.show()

# Save the plot to a file
#fig.savefig('unemployment.png')



# Create a figure and axis to plot on
fig, ax = plt.subplots(figsize=(12, 6))

# Iterate through the dictionary containing the DataFrames for each city
for city, df in merged_time_series.items():
    # Plot the unemployment values for the current city
    if city in north_cities:
      ax.plot(df.index[9::12], df['value_tax'][9::12], label=city)

# Set the title, xlabel, and ylabel
ax.set_title('Taxes North Cities')
ax.set_xlabel('Date')
ax.set_ylabel('Tax Rate')

# Add a legend
ax.legend()

# Display the plot
plt.show()

# Save the plot to a file
#fig.savefig('unemployment.png')





import pickle
import matplotlib.pyplot as plt
from pandas.plotting import autocorrelation_plot

# open the file for reading
with open('merged_time_series', 'rb') as f:
    # deserialize the data and load it back into a dictionary
    merged_time_series = pickle.load(f)


south = [
    "Miami, FL", "Orlando, FL", "Tampa, FL", 
    "Port St. Lucie, FL", "Panama City, FL", "Cape Coral, FL",
    "North Port, FL", "Ocean City, NJ", "Palm Bay, FL", "Crestview, FL",
    "Hilton Head Island, SC", "Charleston, SC",
    "Houston, TX", "San Antonio, TX", "Austin, TX", "New Bern, NC",
    "Tuscaloosa, AL", "Jackson, TN", "Memphis, TN",
    "Tulsa, OK", "El Paso, TX"
]

# Create a figure and axis to plot on
fig, ax = plt.subplots(figsize=(12, 6))

# Iterate through the dictionary containing the DataFrames for each city
for city, df in merged_time_series.items():
    if city in south:
        # Plot the housing prices for the current city
        ax.plot(df.index, df['value'], label=city)

# Set the title, xlabel, and ylabel
ax.set_title('Housing Prices for South Cities')
ax.set_xlabel('Date')
ax.set_ylabel('Housing Price')
#ax.legend()

# Display the legend and show the plot
plt.show()
plt.savefig('housing_prices_north.png')


# Create a figure and axis to plot on
fig, ax = plt.subplots(figsize=(12, 6))

# Iterate through the dictionary containing the DataFrames for each city
for city, df in merged_time_series.items():
    if city in south:
        # Calculate and plot the autocorrelations of the housing prices for the current city
        autocorrelation_plot(df['value'])

# Set the title, xlabel, and ylabel
ax.set_title('Autocorrelations of Housing Prices for South Cities')
ax.set_xlabel('Lag')
ax.set_ylabel('Autocorrelation')
#ax.legend()

# Display the legend and show the plot
plt.show()
plt.savefig('autocorrelation_north.png')


# Create a figure and axis to plot on
fig, ax = plt.subplots(figsize=(12, 6))

# Iterate through the dictionary containing the DataFrames for each city
for city, df in merged_time_series.items():
    # Plot the unemployment values for the current city
    if city in south:
      ax.plot(df.index, df['value_unemployment'], label=city)

# Set the title, xlabel, and ylabel
ax.set_title('Unemployment South Cities')
ax.set_xlabel('Date')
ax.set_ylabel('Unemployment Rate')

# Add a legend
#ax.legend()

# Display the plot
plt.show()

# Save the plot to a file
#fig.savefig('unemployment.png')


# Create a figure and axis to plot on
fig, ax = plt.subplots(figsize=(12, 6))

# Iterate through the dictionary containing the DataFrames for each city
for city, df in merged_time_series.items():
    # Plot the unemployment values for the current city
    if city in south:
      ax.plot(df.index, df['value_income'], label=city)

# Set the title, xlabel, and ylabel
ax.set_title('Income South Cities')
ax.set_xlabel('Date')
ax.set_ylabel('Income Rate')

# Add a legend
#ax.legend()

# Display the plot
plt.show()

# Save the plot to a file
#fig.savefig('unemployment.png')



# Create a figure and axis to plot on
fig, ax = plt.subplots(figsize=(12, 6))

# Iterate through the dictionary containing the DataFrames for each city
for city, df in merged_time_series.items():
    # Plot the unemployment values for the current city
    if city in south:
      ax.plot(df.index, df['value_gdp'], label=city)

# Set the title, xlabel, and ylabel
ax.set_title('GDP South Cities')
ax.set_xlabel('Date')
ax.set_ylabel('GDP Rate')

# Add a legend
#ax.legend()

# Display the plot
plt.show()

# Save the plot to a file
#fig.savefig('unemployment.png')



# Create a figure and axis to plot on
fig, ax = plt.subplots(figsize=(12, 6))

# Iterate through the dictionary containing the DataFrames for each city
for city, df in merged_time_series.items():
    # Plot the unemployment values for the current city
    if city in south:
      ax.plot(df.index, df['value_population'], label=city)

# Set the title, xlabel, and ylabel
ax.set_title('Population South Cities')
ax.set_xlabel('Date')
ax.set_ylabel('Population Rate')

# Add a legend
#ax.legend()

# Display the plot
plt.show()

# Save the plot to a file
#fig.savefig('unemployment.png')


# Create a figure and axis to plot on
fig, ax = plt.subplots(figsize=(12, 6))

# Iterate through the dictionary containing the DataFrames for each city
for city, df in merged_time_series.items():
    # Plot the unemployment values for the current city
    if city in south:
      ax.plot(df.index, df['value_crime'], label=city)

# Set the title, xlabel, and ylabel
ax.set_title('Crimes South Cities')
ax.set_xlabel('Date')
ax.set_ylabel('Crimes Rate')

# Add a legend
#ax.legend()

# Display the plot
plt.show()

# Save the plot to a file
#fig.savefig('unemployment.png')



# Create a figure and axis to plot on
fig, ax = plt.subplots(figsize=(12, 6))

# Iterate through the dictionary containing the DataFrames for each city
for city, df in merged_time_series.items():
    # Plot the unemployment values for the current city
    if city in south:
      ax.plot(df.index[9::12], df['value_tax'][9::12], label=city)

# Set the title, xlabel, and ylabel
ax.set_title('Taxes South Cities')
ax.set_xlabel('Date')
ax.set_ylabel('Tax Rate')

# Add a legend
#ax.legend()

# Display the plot
plt.show()

# Save the plot to a file
#fig.savefig('unemployment.png')




west = [
    "San Diego, CA", "Santa Cruz, CA", "Vallejo, CA", "Santa Rosa, CA", "San Luis Obispo, CA",
    "Redding, CA", "Santa Maria, CA",
    "Medford, OR", "Fresno, CA", "Stockton, CA", "Sacramento, CA", "Riverside, CA",
   "Los Angeles, CA", "Napa, CA", "Kahului, HI", "Salem, OR",
    "Portland, OR", "Reno, NV"
]


import pickle
import matplotlib.pyplot as plt
from pandas.plotting import autocorrelation_plot

# open the file for reading
with open('merged_time_series', 'rb') as f:
    # deserialize the data and load it back into a dictionary
    merged_time_series = pickle.load(f)


# Create a figure and axis to plot on
fig, ax = plt.subplots(figsize=(12, 6))

# Iterate through the dictionary containing the DataFrames for each city
for city, df in merged_time_series.items():
    if city in west:
        # Plot the housing prices for the current city
        ax.plot(df.index, df['value'], label=city)

# Set the title, xlabel, and ylabel
ax.set_title('Housing Prices for West Cities')
ax.set_xlabel('Date')
ax.set_ylabel('Housing Price')
#ax.legend()

# Display the legend and show the plot
plt.show()
plt.savefig('housing_prices_north.png')


# Create a figure and axis to plot on
fig, ax = plt.subplots(figsize=(12, 6))

# Iterate through the dictionary containing the DataFrames for each city
for city, df in merged_time_series.items():
    if city in west:
        # Calculate and plot the autocorrelations of the housing prices for the current city
        autocorrelation_plot(df['value'])

# Set the title, xlabel, and ylabel
ax.set_title('Autocorrelations of Housing Prices for West Cities')
ax.set_xlabel('Lag')
ax.set_ylabel('Autocorrelation')

# Display the legend and show the plot
plt.show()
plt.savefig('autocorrelation_north.png')


# Create a figure and axis to plot on
fig, ax = plt.subplots(figsize=(12, 6))

# Iterate through the dictionary containing the DataFrames for each city
for city, df in merged_time_series.items():
    # Plot the unemployment values for the current city
    if city in west:
      ax.plot(df.index, df['value_unemployment'], label=city)

# Set the title, xlabel, and ylabel
ax.set_title('Unemployment West Cities')
ax.set_xlabel('Date')
ax.set_ylabel('Unemployment Rate')

# Add a legend
#ax.legend()

# Display the plot
plt.show()

# Save the plot to a file
#fig.savefig('unemployment.png')


# Create a figure and axis to plot on
fig, ax = plt.subplots(figsize=(12, 6))

# Iterate through the dictionary containing the DataFrames for each city
for city, df in merged_time_series.items():
    # Plot the unemployment values for the current city
    if city in west:
      ax.plot(df.index, df['value_income'], label=city)

# Set the title, xlabel, and ylabel
ax.set_title('Income West Cities')
ax.set_xlabel('Date')
ax.set_ylabel('Income Rate')

# Add a legend
#ax.legend()

# Display the plot
plt.show()

# Save the plot to a file
#fig.savefig('unemployment.png')



# Create a figure and axis to plot on
fig, ax = plt.subplots(figsize=(12, 6))

# Iterate through the dictionary containing the DataFrames for each city
for city, df in merged_time_series.items():
    # Plot the unemployment values for the current city
    if city in west:
      ax.plot(df.index, df['value_gdp'], label=city)

# Set the title, xlabel, and ylabel
ax.set_title('GDP West Cities')
ax.set_xlabel('Date')
ax.set_ylabel('GDP Rate')

# Add a legend
#ax.legend()

# Display the plot
plt.show()

# Save the plot to a file
#fig.savefig('unemployment.png')



# Create a figure and axis to plot on
fig, ax = plt.subplots(figsize=(12, 6))

# Iterate through the dictionary containing the DataFrames for each city
for city, df in merged_time_series.items():
    # Plot the unemployment values for the current city
    if city in west:
      ax.plot(df.index, df['value_population'], label=city)

# Set the title, xlabel, and ylabel
ax.set_title('Population West Cities')
ax.set_xlabel('Date')
ax.set_ylabel('Population Rate')

# Add a legend
#ax.legend()

# Display the plot
plt.show()

# Save the plot to a file
#fig.savefig('unemployment.png')


# Create a figure and axis to plot on
fig, ax = plt.subplots(figsize=(12, 6))

# Iterate through the dictionary containing the DataFrames for each city
for city, df in merged_time_series.items():
    # Plot the unemployment values for the current city
    if city in west:
      ax.plot(df.index, df['value_crime'], label=city)

# Set the title, xlabel, and ylabel
ax.set_title('Crimes West Cities')
ax.set_xlabel('Date')
ax.set_ylabel('Crimes Rate')

# Add a legend
#ax.legend()

# Display the plot
plt.show()

# Save the plot to a file
#fig.savefig('unemployment.png')



# Create a figure and axis to plot on
fig, ax = plt.subplots(figsize=(12, 6))

# Iterate through the dictionary containing the DataFrames for each city
for city, df in merged_time_series.items():
    # Plot the unemployment values for the current city
    if city in west:
      ax.plot(df.index[9::12], df['value_tax'][9::12], label=city)

# Set the title, xlabel, and ylabel
ax.set_title('Taxes West Cities')
ax.set_xlabel('Date')
ax.set_ylabel('Tax Rate')

# Add a legend
#ax.legend()

# Display the plot
plt.show()

# Save the plot to a file
#fig.savefig('unemployment.png')





east = [
    "Baltimore, MD", "Hagerstown, MD", "Atlantic City, NJ", "Vineland, NJ", "Washington, VA",
    "Ithaca, NY", "Albany, NY", "York, PA", "Altoona, PA", "Reading, PA", "Trenton, NJ",
    "Kingston, NY", "California, MD"
]

import pickle
import matplotlib.pyplot as plt
from pandas.plotting import autocorrelation_plot

# open the file for reading
with open('merged_time_series', 'rb') as f:
    # deserialize the data and load it back into a dictionary
    merged_time_series = pickle.load(f)


# Create a figure and axis to plot on
fig, ax = plt.subplots(figsize=(12, 6))

# Iterate through the dictionary containing the DataFrames for each city
for city, df in merged_time_series.items():
    if city in east:
        # Plot the housing prices for the current city
        ax.plot(df.index, df['value'], label=city)

# Set the title, xlabel, and ylabel
ax.set_title('Housing Prices for East Cities')
ax.set_xlabel('Date')
ax.set_ylabel('Housing Price')
ax.legend()

# Display the legend and show the plot
plt.show()
plt.savefig('housing_prices_north.png')


# Create a figure and axis to plot on
fig, ax = plt.subplots(figsize=(12, 6))

# Iterate through the dictionary containing the DataFrames for each city
for city, df in merged_time_series.items():
    if city in east:
        # Calculate and plot the autocorrelations of the housing prices for the current city
        autocorrelation_plot(df['value'])

# Set the title, xlabel, and ylabel
ax.set_title('Autocorrelations of Housing Prices for East Cities')
ax.set_xlabel('Lag')
ax.set_ylabel('Autocorrelation')

# Display the legend and show the plot
plt.show()
plt.savefig('autocorrelation_north.png')


# Create a figure and axis to plot on
fig, ax = plt.subplots(figsize=(12, 6))

# Iterate through the dictionary containing the DataFrames for each city
for city, df in merged_time_series.items():
    # Plot the unemployment values for the current city
    if city in east:
      ax.plot(df.index, df['value_unemployment'], label=city)

# Set the title, xlabel, and ylabel
ax.set_title('Unemployment East Cities')
ax.set_xlabel('Date')
ax.set_ylabel('Unemployment Rate')

# Add a legend
ax.legend()

# Display the plot
plt.show()

# Save the plot to a file
#fig.savefig('unemployment.png')


# Create a figure and axis to plot on
fig, ax = plt.subplots(figsize=(12, 6))

# Iterate through the dictionary containing the DataFrames for each city
for city, df in merged_time_series.items():
    # Plot the unemployment values for the current city
    if city in east:
      ax.plot(df.index, df['value_income'], label=city)

# Set the title, xlabel, and ylabel
ax.set_title('Income East Cities')
ax.set_xlabel('Date')
ax.set_ylabel('Income Rate')

# Add a legend
ax.legend()

# Display the plot
plt.show()

# Save the plot to a file
#fig.savefig('unemployment.png')



# Create a figure and axis to plot on
fig, ax = plt.subplots(figsize=(12, 6))

# Iterate through the dictionary containing the DataFrames for each city
for city, df in merged_time_series.items():
    # Plot the unemployment values for the current city
    if city in east:
      ax.plot(df.index, df['value_gdp'], label=city)

# Set the title, xlabel, and ylabel
ax.set_title('GDP East Cities')
ax.set_xlabel('Date')
ax.set_ylabel('GDP Rate')

# Add a legend
ax.legend()

# Display the plot
plt.show()

# Save the plot to a file
#fig.savefig('unemployment.png')



# Create a figure and axis to plot on
fig, ax = plt.subplots(figsize=(12, 6))

# Iterate through the dictionary containing the DataFrames for each city
for city, df in merged_time_series.items():
    # Plot the unemployment values for the current city
    if city in east:
      ax.plot(df.index, df['value_population'], label=city)

# Set the title, xlabel, and ylabel
ax.set_title('Population East Cities')
ax.set_xlabel('Date')
ax.set_ylabel('Population Rate')

# Add a legend
ax.legend()

# Display the plot
plt.show()

# Save the plot to a file
#fig.savefig('unemployment.png')


# Create a figure and axis to plot on
fig, ax = plt.subplots(figsize=(12, 6))

# Iterate through the dictionary containing the DataFrames for each city
for city, df in merged_time_series.items():
    # Plot the unemployment values for the current city
    if city in east:
      ax.plot(df.index, df['value_crime'], label=city)

# Set the title, xlabel, and ylabel
ax.set_title('Crimes East Cities')
ax.set_xlabel('Date')
ax.set_ylabel('Crimes Rate')

# Add a legend
ax.legend()

# Display the plot
plt.show()

# Save the plot to a file
#fig.savefig('unemployment.png')



# Create a figure and axis to plot on
fig, ax = plt.subplots(figsize=(12, 6))

# Iterate through the dictionary containing the DataFrames for each city
for city, df in merged_time_series.items():
    # Plot the unemployment values for the current city
    if city in east:
      ax.plot(df.index[9::12], df['value_tax'][9::12], label=city)

# Set the title, xlabel, and ylabel
ax.set_title('Taxes East Cities')
ax.set_xlabel('Date')
ax.set_ylabel('Tax Rate')

# Add a legend
ax.legend()

# Display the plot
plt.show()

# Save the plot to a file
#fig.savefig('unemployment.png')





northwest = [
    "Idaho Falls, ID", "Greeley, CO", "Boulder, CO", "Colorado Springs, CO", "Pine Bluff, AR",
    "Asheville, NC", "Cedar Rapids, IA", "Des Moines, IA", "Pueblo, CO", "Lincoln, NE",
    "Ogden, UT", "Salt Lake City, UT", "Seattle, WA", "Spokane, WA", "Boise, ID",
    "Billings, MT", "Missoula, MT", "Anchorage, AK", "Fairbanks, AK", "Juneau, AK"
]
import pickle
import matplotlib.pyplot as plt
from pandas.plotting import autocorrelation_plot

# open the file for reading
with open('merged_time_series', 'rb') as f:
    # deserialize the data and load it back into a dictionary
    merged_time_series = pickle.load(f)


# Create a figure and axis to plot on
fig, ax = plt.subplots(figsize=(12, 6))

# Iterate through the dictionary containing the DataFrames for each city
for city, df in merged_time_series.items():
    if city in northwest:
        # Plot the housing prices for the current city
        ax.plot(df.index, df['value'], label=city)

# Set the title, xlabel, and ylabel
ax.set_title('Housing Prices for NW Cities')
ax.set_xlabel('Date')
ax.set_ylabel('Housing Price')
ax.legend()

# Display the legend and show the plot
plt.show()
plt.savefig('housing_prices_north.png')


# Create a figure and axis to plot on
fig, ax = plt.subplots(figsize=(12, 6))

# Iterate through the dictionary containing the DataFrames for each city
for city, df in merged_time_series.items():
    if city in northwest:
        # Calculate and plot the autocorrelations of the housing prices for the current city
        autocorrelation_plot(df['value'])

# Set the title, xlabel, and ylabel
ax.set_title('Autocorrelations of Housing Prices for NW Cities')
ax.set_xlabel('Lag')
ax.set_ylabel('Autocorrelation')

# Display the legend and show the plot
plt.show()
plt.savefig('autocorrelation_north.png')


# Create a figure and axis to plot on
fig, ax = plt.subplots(figsize=(12, 6))

# Iterate through the dictionary containing the DataFrames for each city
for city, df in merged_time_series.items():
    # Plot the unemployment values for the current city
    if city in northwest:
      ax.plot(df.index, df['value_unemployment'], label=city)

# Set the title, xlabel, and ylabel
ax.set_title('Unemployment NW Cities')
ax.set_xlabel('Date')
ax.set_ylabel('Unemployment Rate')

# Add a legend
ax.legend()

# Display the plot
plt.show()

# Save the plot to a file
#fig.savefig('unemployment.png')


# Create a figure and axis to plot on
fig, ax = plt.subplots(figsize=(12, 6))

# Iterate through the dictionary containing the DataFrames for each city
for city, df in merged_time_series.items():
    # Plot the unemployment values for the current city
    if city in northwest:
      ax.plot(df.index, df['value_income'], label=city)

# Set the title, xlabel, and ylabel
ax.set_title('Income NW Cities')
ax.set_xlabel('Date')
ax.set_ylabel('Income Rate')

# Add a legend
ax.legend()

# Display the plot
plt.show()

# Save the plot to a file
#fig.savefig('unemployment.png')



# Create a figure and axis to plot on
fig, ax = plt.subplots(figsize=(12, 6))

# Iterate through the dictionary containing the DataFrames for each city
for city, df in merged_time_series.items():
    # Plot the unemployment values for the current city
    if city in northwest:
      ax.plot(df.index, df['value_gdp'], label=city)

# Set the title, xlabel, and ylabel
ax.set_title('GDP NW Cities')
ax.set_xlabel('Date')
ax.set_ylabel('GDP Rate')

# Add a legend
ax.legend()

# Display the plot
plt.show()

# Save the plot to a file
#fig.savefig('unemployment.png')



# Create a figure and axis to plot on
fig, ax = plt.subplots(figsize=(12, 6))

# Iterate through the dictionary containing the DataFrames for each city
for city, df in merged_time_series.items():
    # Plot the unemployment values for the current city
    if city in northwest:
      ax.plot(df.index, df['value_population'], label=city)

# Set the title, xlabel, and ylabel
ax.set_title('Population NW Cities')
ax.set_xlabel('Date')
ax.set_ylabel('Population Rate')

# Add a legend
ax.legend()

# Display the plot
plt.show()

# Save the plot to a file
#fig.savefig('unemployment.png')


# Create a figure and axis to plot on
fig, ax = plt.subplots(figsize=(12, 6))

# Iterate through the dictionary containing the DataFrames for each city
for city, df in merged_time_series.items():
    # Plot the unemployment values for the current city
    if city in northwest:
      ax.plot(df.index, df['value_crime'], label=city)

# Set the title, xlabel, and ylabel
ax.set_title('Crimes NW Cities')
ax.set_xlabel('Date')
ax.set_ylabel('Crimes Rate')

# Add a legend
ax.legend()

# Display the plot
plt.show()

# Save the plot to a file
#fig.savefig('unemployment.png')



# Create a figure and axis to plot on
fig, ax = plt.subplots(figsize=(12, 6))

# Iterate through the dictionary containing the DataFrames for each city
for city, df in merged_time_series.items():
    # Plot the unemployment values for the current city
    if city in northwest:
      ax.plot(df.index[9::12], df['value_tax'][9::12], label=city)

# Set the title, xlabel, and ylabel
ax.set_title('Taxes NW Cities')
ax.set_xlabel('Date')
ax.set_ylabel('Tax Rate')

# Add a legend
ax.legend()

# Display the plot
plt.show()

# Save the plot to a file
#fig.savefig('unemployment.png')

import pickle
import matplotlib.pyplot as plt
from pandas.plotting import autocorrelation_plot

# open the file for reading
with open('merged_time_series', 'rb') as f:
    # deserialize the data and load it back into a dictionary
    merged_time_series = pickle.load(f)

northeast = [
    "Niles, MI", "Bay City, MI", "Lansing, MI", "Midland, MI", "Cincinnati, OH", "Cleveland, TN",
    "Muskegon, MI", "Toledo, OH", "Detroit, MI",
    "Chicago, IL", "Lafayette, IN", "Akron, OH", "Boston, MA", "Providence, RI",
    "Hartford, CT", "Springfield, MA", "Worcester, MA", "Burlington, VT",
    "Manchester, NH", "Portland, ME"
]
# Create a figure and axis to plot on
fig, ax = plt.subplots(figsize=(12, 6))

# Iterate through the dictionary containing the DataFrames for each city
for city, df in merged_time_series.items():
    if city in northeast:
        # Plot the housing prices for the current city
        ax.plot(df.index, df['value'], label=city)

# Set the title, xlabel, and ylabel
ax.set_title('Housing Prices for NE Cities')
ax.set_xlabel('Date')
ax.set_ylabel('Housing Price')
ax.legend()

# Display the legend and show the plot
plt.show()
plt.savefig('housing_prices_north.png')


# Create a figure and axis to plot on
fig, ax = plt.subplots(figsize=(12, 6))

# Iterate through the dictionary containing the DataFrames for each city
for city, df in merged_time_series.items():
    if city in northeast:
        # Calculate and plot the autocorrelations of the housing prices for the current city
        autocorrelation_plot(df['value'])

# Set the title, xlabel, and ylabel
ax.set_title('Autocorrelations of Housing Prices for NE Cities')
ax.set_xlabel('Lag')
ax.set_ylabel('Autocorrelation')

# Display the legend and show the plot
plt.show()
plt.savefig('autocorrelation_north.png')


# Create a figure and axis to plot on
fig, ax = plt.subplots(figsize=(12, 6))

# Iterate through the dictionary containing the DataFrames for each city
for city, df in merged_time_series.items():
    # Plot the unemployment values for the current city
    if city in northeast:
      ax.plot(df.index, df['value_unemployment'], label=city)

# Set the title, xlabel, and ylabel
ax.set_title('Unemployment NE Cities')
ax.set_xlabel('Date')
ax.set_ylabel('Unemployment Rate')

# Add a legend
ax.legend()

# Display the plot
plt.show()

# Save the plot to a file
#fig.savefig('unemployment.png')


# Create a figure and axis to plot on
fig, ax = plt.subplots(figsize=(12, 6))

# Iterate through the dictionary containing the DataFrames for each city
for city, df in merged_time_series.items():
    # Plot the unemployment values for the current city
    if city in northeast:
      ax.plot(df.index, df['value_income'], label=city)

# Set the title, xlabel, and ylabel
ax.set_title('Income NE Cities')
ax.set_xlabel('Date')
ax.set_ylabel('Income Rate')

# Add a legend
ax.legend()

# Display the plot
plt.show()

# Save the plot to a file
#fig.savefig('unemployment.png')



# Create a figure and axis to plot on
fig, ax = plt.subplots(figsize=(12, 6))

# Iterate through the dictionary containing the DataFrames for each city
for city, df in merged_time_series.items():
    # Plot the unemployment values for the current city
    if city in northeast:
      ax.plot(df.index, df['value_gdp'], label=city)

# Set the title, xlabel, and ylabel
ax.set_title('GDP NE Cities')
ax.set_xlabel('Date')
ax.set_ylabel('GDP Rate')

# Add a legend
ax.legend()

# Display the plot
plt.show()

# Save the plot to a file
#fig.savefig('unemployment.png')



# Create a figure and axis to plot on
fig, ax = plt.subplots(figsize=(12, 6))

# Iterate through the dictionary containing the DataFrames for each city
for city, df in merged_time_series.items():
    # Plot the unemployment values for the current city
    if city in northeast:
      ax.plot(df.index, df['value_population'], label=city)

# Set the title, xlabel, and ylabel
ax.set_title('Population NE Cities')
ax.set_xlabel('Date')
ax.set_ylabel('Population Rate')

# Add a legend
ax.legend()

# Display the plot
plt.show()

# Save the plot to a file
#fig.savefig('unemployment.png')


# Create a figure and axis to plot on
fig, ax = plt.subplots(figsize=(12, 6))

# Iterate through the dictionary containing the DataFrames for each city
for city, df in merged_time_series.items():
    # Plot the unemployment values for the current city
    if city in northeast:
      ax.plot(df.index, df['value_crime'], label=city)

# Set the title, xlabel, and ylabel
ax.set_title('Crimes NE Cities')
ax.set_xlabel('Date')
ax.set_ylabel('Crimes Rate')

# Add a legend
ax.legend()

# Display the plot
plt.show()

# Save the plot to a file
#fig.savefig('unemployment.png')



# Create a figure and axis to plot on
fig, ax = plt.subplots(figsize=(12, 6))

# Iterate through the dictionary containing the DataFrames for each city
for city, df in merged_time_series.items():
    # Plot the unemployment values for the current city
    if city in northeast:
      ax.plot(df.index[9::12], df['value_tax'][9::12], label=city)

# Set the title, xlabel, and ylabel
ax.set_title('Taxes NE Cities')
ax.set_xlabel('Date')
ax.set_ylabel('Tax Rate')

# Add a legend
ax.legend()

# Display the plot
plt.show()

# Save the plot to a file
#fig.savefig('unemployment.png')


import pickle
import matplotlib.pyplot as plt
from pandas.plotting import autocorrelation_plot

# open the file for reading
with open('merged_time_series', 'rb') as f:
    # deserialize the data and load it back into a dictionary
    merged_time_series = pickle.load(f)

southeast = [
    "Rocky Mount, NC", "Raleigh, NC", "Greenville, SC",
    "Hickory, NC", "Hot Springs, AR", "Monroe, MI", "Greensboro, NC",
    "Bowling Green, KY", "Goldsboro, NC", "Fayetteville, NC",
    "Evansville, IN", "Jonesboro, AR", "Columbus, OH", 
    "Tuscaloosa, AL", "Atlanta, GA", 
    "Jackson, MS", "New Orleans, LA", "Mobile, AL", "Charleston, WV",
    "Fort Smith, AR", "Nashville, TN", "Charlotte, NC", 
    "Orlando, FL", "Tampa, FL", "Miami, FL", "Jacksonville, FL", "Fort Lauderdale, FL",
    "West Palm Beach, FL", "Sarasota, FL", "Fort Myers, FL"
]
# Create a figure and axis to plot on
fig, ax = plt.subplots(figsize=(12, 6))

# Iterate through the dictionary containing the DataFrames for each city
for city, df in merged_time_series.items():
    if city in southeast:
        # Plot the housing prices for the current city
        ax.plot(df.index, df['value'], label=city)

# Set the title, xlabel, and ylabel
ax.set_title('Housing Prices for SE Cities')
ax.set_xlabel('Date')
ax.set_ylabel('Housing Price')
#ax.legend()

# Display the legend and show the plot
plt.show()
plt.savefig('housing_prices_north.png')


# Create a figure and axis to plot on
fig, ax = plt.subplots(figsize=(12, 6))

# Iterate through the dictionary containing the DataFrames for each city
for city, df in merged_time_series.items():
    if city in southeast:
        # Calculate and plot the autocorrelations of the housing prices for the current city
        autocorrelation_plot(df['value'])

# Set the title, xlabel, and ylabel
ax.set_title('Autocorrelations of Housing Prices for SE Cities')
ax.set_xlabel('Lag')
ax.set_ylabel('Autocorrelation')

# Display the legend and show the plot
plt.show()
plt.savefig('autocorrelation_north.png')


# Create a figure and axis to plot on
fig, ax = plt.subplots(figsize=(12, 6))

# Iterate through the dictionary containing the DataFrames for each city
for city, df in merged_time_series.items():
    # Plot the unemployment values for the current city
    if city in southeast:
      ax.plot(df.index, df['value_unemployment'], label=city)

# Set the title, xlabel, and ylabel
ax.set_title('Unemployment SE Cities')
ax.set_xlabel('Date')
ax.set_ylabel('Unemployment Rate')

# Add a legend
#ax.legend()

# Display the plot
plt.show()

# Save the plot to a file
#fig.savefig('unemployment.png')


# Create a figure and axis to plot on
fig, ax = plt.subplots(figsize=(12, 6))

# Iterate through the dictionary containing the DataFrames for each city
for city, df in merged_time_series.items():
    # Plot the unemployment values for the current city
    if city in southeast:
      ax.plot(df.index, df['value_income'], label=city)

# Set the title, xlabel, and ylabel
ax.set_title('Income SE Cities')
ax.set_xlabel('Date')
ax.set_ylabel('Income Rate')

# Add a legend
#ax.legend()

# Display the plot
plt.show()

# Save the plot to a file
#fig.savefig('unemployment.png')



# Create a figure and axis to plot on
fig, ax = plt.subplots(figsize=(12, 6))

# Iterate through the dictionary containing the DataFrames for each city
for city, df in merged_time_series.items():
    # Plot the unemployment values for the current city
    if city in southeast:
      ax.plot(df.index, df['value_gdp'], label=city)

# Set the title, xlabel, and ylabel
ax.set_title('GDP SE Cities')
ax.set_xlabel('Date')
ax.set_ylabel('GDP Rate')

# Add a legend
#ax.legend()

# Display the plot
plt.show()

# Save the plot to a file
#fig.savefig('unemployment.png')



# Create a figure and axis to plot on
fig, ax = plt.subplots(figsize=(12, 6))

# Iterate through the dictionary containing the DataFrames for each city
for city, df in merged_time_series.items():
    # Plot the unemployment values for the current city
    if city in southeast:
      ax.plot(df.index, df['value_population'], label=city)

# Set the title, xlabel, and ylabel
ax.set_title('Population SE Cities')
ax.set_xlabel('Date')
ax.set_ylabel('Population Rate')

# Add a legend
#ax.legend()

# Display the plot
plt.show()

# Save the plot to a file
#fig.savefig('unemployment.png')


# Create a figure and axis to plot on
fig, ax = plt.subplots(figsize=(12, 6))

# Iterate through the dictionary containing the DataFrames for each city
for city, df in merged_time_series.items():
    # Plot the unemployment values for the current city
    if city in southeast:
      ax.plot(df.index, df['value_crime'], label=city)

# Set the title, xlabel, and ylabel
ax.set_title('Crimes SE Cities')
ax.set_xlabel('Date')
ax.set_ylabel('Crimes Rate')

# Add a legend
#ax.legend()

# Display the plot
plt.show()

# Save the plot to a file
#fig.savefig('unemployment.png')



# Create a figure and axis to plot on
fig, ax = plt.subplots(figsize=(12, 6))

# Iterate through the dictionary containing the DataFrames for each city
for city, df in merged_time_series.items():
    # Plot the unemployment values for the current city
    if city in southeast:
      ax.plot(df.index[9::12], df['value_tax'][9::12], label=city)

# Set the title, xlabel, and ylabel
ax.set_title('Taxes SE Cities')
ax.set_xlabel('Date')
ax.set_ylabel('Tax Rate')

# Add a legend
#ax.legend()

# Display the plot
plt.show()

# Save the plot to a file
#fig.savefig('unemployment.png')




import pickle
import matplotlib.pyplot as plt
from pandas.plotting import autocorrelation_plot

# open the file for reading
with open('merged_time_series', 'rb') as f:
    # deserialize the data and load it back into a dictionary
    merged_time_series = pickle.load(f)

southwest = [
    "Omaha, NE", "Danville, IL", "Santa Fe, NM", "El Paso, TX", "Oklahoma City, OK",
    "Tucson, AZ", "Las Vegas, NV", "Riverside, CA",
    "Palm Springs, CA", "San Diego, CA", "Los Angeles, CA", "Santa Barbara, CA",
    "San Francisco, CA", "Oakland, CA", "San Jose, CA", "Sacramento, CA",
    "Bakersfield, CA", "Reno, NV", "Salt Lake City, UT", "Denver, CO",
    "Pueblo, CO",  "Midland, TX",
    "Odessa, TX", "San Angelo, TX", "Dallas, TX",
    "Fort Worth, TX", "Austin, TX", "San Antonio, TX", "Houston, TX",
    "Beaumont, TX", "Port Arthur, TX",  "Lafayette, LA"
]
# Create a figure and axis to plot on
fig, ax = plt.subplots(figsize=(12, 6))

# Iterate through the dictionary containing the DataFrames for each city
for city, df in merged_time_series.items():
    if city in southwest:
        # Plot the housing prices for the current city
        ax.plot(df.index, df['value'], label=city)

# Set the title, xlabel, and ylabel
ax.set_title('Housing Prices for SW Cities')
ax.set_xlabel('Date')
ax.set_ylabel('Housing Price')
ax.legend()

# Display the legend and show the plot
plt.show()
plt.savefig('housing_prices_north.png')


# Create a figure and axis to plot on
fig, ax = plt.subplots(figsize=(12, 6))

# Iterate through the dictionary containing the DataFrames for each city
for city, df in merged_time_series.items():
    if city in southwest:
        # Calculate and plot the autocorrelations of the housing prices for the current city
        autocorrelation_plot(df['value'])

# Set the title, xlabel, and ylabel
ax.set_title('Autocorrelations of Housing Prices for SW Cities')
ax.set_xlabel('Lag')
ax.set_ylabel('Autocorrelation')

# Display the legend and show the plot
plt.show()
plt.savefig('autocorrelation_north.png')


# Create a figure and axis to plot on
fig, ax = plt.subplots(figsize=(12, 6))

# Iterate through the dictionary containing the DataFrames for each city
for city, df in merged_time_series.items():
    # Plot the unemployment values for the current city
    if city in southwest:
      ax.plot(df.index, df['value_unemployment'], label=city)

# Set the title, xlabel, and ylabel
ax.set_title('Unemployment SW Cities')
ax.set_xlabel('Date')
ax.set_ylabel('Unemployment Rate')

# Add a legend
ax.legend()

# Display the plot
plt.show()

# Save the plot to a file
#fig.savefig('unemployment.png')


# Create a figure and axis to plot on
fig, ax = plt.subplots(figsize=(12, 6))

# Iterate through the dictionary containing the DataFrames for each city
for city, df in merged_time_series.items():
    # Plot the unemployment values for the current city
    if city in southwest:
      ax.plot(df.index, df['value_income'], label=city)

# Set the title, xlabel, and ylabel
ax.set_title('Income SW Cities')
ax.set_xlabel('Date')
ax.set_ylabel('Income Rate')

# Add a legend
ax.legend()

# Display the plot
plt.show()

# Save the plot to a file
#fig.savefig('unemployment.png')



# Create a figure and axis to plot on
fig, ax = plt.subplots(figsize=(12, 6))

# Iterate through the dictionary containing the DataFrames for each city
for city, df in merged_time_series.items():
    # Plot the unemployment values for the current city
    if city in southwest:
      ax.plot(df.index, df['value_gdp'], label=city)

# Set the title, xlabel, and ylabel
ax.set_title('GDP SW Cities')
ax.set_xlabel('Date')
ax.set_ylabel('GDP Rate')

# Add a legend
ax.legend()

# Display the plot
plt.show()

# Save the plot to a file
#fig.savefig('unemployment.png')



# Create a figure and axis to plot on
fig, ax = plt.subplots(figsize=(12, 6))

# Iterate through the dictionary containing the DataFrames for each city
for city, df in merged_time_series.items():
    # Plot the unemployment values for the current city
    if city in southwest:
      ax.plot(df.index, df['value_population'], label=city)

# Set the title, xlabel, and ylabel
ax.set_title('Population SW Cities')
ax.set_xlabel('Date')
ax.set_ylabel('Population Rate')

# Add a legend
ax.legend()

# Display the plot
plt.show()

# Save the plot to a file
#fig.savefig('unemployment.png')


# Create a figure and axis to plot on
fig, ax = plt.subplots(figsize=(12, 6))

# Iterate through the dictionary containing the DataFrames for each city
for city, df in merged_time_series.items():
    # Plot the unemployment values for the current city
    if city in southwest:
      ax.plot(df.index, df['value_crime'], label=city)

# Set the title, xlabel, and ylabel
ax.set_title('Crimes SW Cities')
ax.set_xlabel('Date')
ax.set_ylabel('Crimes Rate')

# Add a legend
ax.legend()

# Display the plot
plt.show()

# Save the plot to a file
#fig.savefig('unemployment.png')



# Create a figure and axis to plot on
fig, ax = plt.subplots(figsize=(12, 6))

# Iterate through the dictionary containing the DataFrames for each city
for city, df in merged_time_series.items():
    # Plot the unemployment values for the current city
    if city in southwest:
      ax.plot(df.index[9::12], df['value_tax'][9::12], label=city)

# Set the title, xlabel, and ylabel
ax.set_title('Taxes SW Cities')
ax.set_xlabel('Date')
ax.set_ylabel('Tax Rate')

# Add a legend
ax.legend()

# Display the plot
plt.show()

# Save the plot to a file
#fig.savefig('unemployment.png')


print(merged_time_series["Oxnard, CA"].columns)

print(type(merged_time_series))
for k,v in merged_time_series.items():
  #print(k)
  continue
# Create a figure and axis to plot on
fig, ax = plt.subplots(figsize=(12, 6))

# Iterate through the dictionary containing the DataFrames for each city
for city, df in merged_time_series.items():
    # Plot the unemployment values for the current city
    ax.plot(df.index, df['value_unemployment'], label=city)

# Set the title, xlabel, and ylabel
ax.set_title('Unemployment')
ax.set_xlabel('Date')
ax.set_ylabel('Unemployment Rate')

# Add a legend
#ax.legend()

# Display the plot
plt.show()

# Save the plot to a file
#fig.savefig('unemployment.png')



# Create a figure and axis to plot on
fig, ax = plt.subplots(figsize=(12, 6))

# Iterate through the dictionary containing the DataFrames for each city
for city, df in merged_time_series.items():
    # Plot the unemployment values for the current city
    ax.plot(df.index, df['value_income'], label=city)

# Set the title, xlabel, and ylabel
ax.set_title('Income')
ax.set_xlabel('Date')
ax.set_ylabel('Income Rate')

# Add a legend
#ax.legend()

# Display the plot
plt.show()

# Save the plot to a file
#fig.savefig('unemployment.png')


# Create a figure and axis to plot on
fig, ax = plt.subplots(figsize=(12, 6))

# Iterate through the dictionary containing the DataFrames for each city
for city, df in merged_time_series.items():
    # Plot the unemployment values for the current city
    ax.plot(df.index, df['value_gdp'], label=city)

# Set the title, xlabel, and ylabel
ax.set_title('GDP')
ax.set_xlabel('Date')
ax.set_ylabel('GDP Rate')

# Add a legend
# ax.legend()

# Display the plot
plt.show()

# Save the plot to a file
#fig.savefig('unemployment.png')



# Create a figure and axis to plot on
fig, ax = plt.subplots(figsize=(12, 6))

# Iterate through the dictionary containing the DataFrames for each city
for city, df in merged_time_series.items():
    # Plot the unemployment values for the current city
    ax.plot(df.index, df['value_population'], label=city)

# Set the title, xlabel, and ylabel
ax.set_title('Population')
ax.set_xlabel('Date')
ax.set_ylabel('Population Rate')

# Add a legend
#ax.legend()

# Display the plot
plt.show()

# Save the plot to a file
#fig.savefig('unemployment.png')



print(merged_time_series["Oxnard, CA"].columns)

print(type(merged_time_series))
for city,df in merged_time_series.items():
  print(df.index, df['value_population'])
  continue
# Create a figure and axis to plot on
fig, ax = plt.subplots(figsize=(12, 6))

# Iterate through the dictionary containing the DataFrames for each city
for city, df in merged_time_series.items():
    # Plot the unemployment values for the current city
    ax.plot(df.index, df['value_crime'], label=city)

# Set the title, xlabel, and ylabel
ax.set_title('Crimes')
ax.set_xlabel('Date')
ax.set_ylabel('Crimes Rate')

# Add a legend
#ax.legend()

# Display the plot
plt.show()

# Save the plot to a file
#fig.savefig('unemployment.png')

# Create a figure and axis to plot on
fig, ax = plt.subplots(figsize=(12, 6))

# Iterate through the dictionary containing the DataFrames for each city
for city, df in merged_time_series.items():
    # Plot the unemployment values for the current city
    ax.plot(df.index[9::12], df['value_tax'][9::12], label=city)

# Set the title, xlabel, and ylabel
ax.set_title('Taxes')
ax.set_xlabel('Date')
ax.set_ylabel('Tax Rate')

# Add a legend
#ax.legend()

# Display the plot
plt.show()

# Save the plot to a file
#fig.savefig('unemployment.png')

# Create a figure and axis to plot on
fig, ax = plt.subplots(figsize=(12, 6))

# Iterate through the dictionary containing the DataFrames for each city
for city, df in merged_time_series.items():
    # Plot the unemployment values for the current city
    ax.plot(df.index, df['value_cpi'], label=city)

# Set the title, xlabel, and ylabel
ax.set_title('CPI')
ax.set_xlabel('Date')
ax.set_ylabel('CPI Rate')

# Add a legend
#ax.legend()

# Display the plot
plt.show()

# Save the plot to a file
#fig.savefig('unemployment.png')


# Create a figure and axis to plot on
fig, ax = plt.subplots(figsize=(12, 6))

# Iterate through the dictionary containing the DataFrames for each city
for city, df in merged_time_series.items():
    # Plot the unemployment values for the current city
    ax.plot(df.index, df['value_interest'], label=city)

# Set the title, xlabel, and ylabel
ax.set_title('Interest')
ax.set_xlabel('Date')
ax.set_ylabel('Interest Rate')

# Add a legend
#ax.legend()

# Display the plot
plt.show()

# Save the plot to a file
#fig.savefig('unemployment.png')






































