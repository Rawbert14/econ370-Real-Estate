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
    # Plot the housing prices for the current city
    ax.plot(df.index, df['value'], label=city)

# Set the title, xlabel, and ylabel
ax.set_title('Housing Prices for All Cities')
ax.set_xlabel('Date')
ax.set_ylabel('Housing Price')

# Display the legend and show the plot
plt.show()
plt.savefig('housing_prices')


# Create a figure and axis to plot on
fig, ax = plt.subplots(figsize=(12, 6))

# Iterate through the dictionary containing the DataFrames for each city
for city, df in merged_time_series.items():
    # Calculate and plot the autocorrelations of the housing prices for the current city
    autocorrelation_plot(df['value'])

# Set the title, xlabel, and ylabel
ax.set_title('Autocorrelations of Housing Prices for All Cities')
ax.set_xlabel('Lag')
ax.set_ylabel('Autocorrelation')

# Display the legend and show the plot
plt.show()
plt.savefig('autocorrelation.png')
