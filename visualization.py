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
ax.legend()

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

print(merged_time_series["Oxnard, CA"].columns)

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



