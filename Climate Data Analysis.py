#!/usr/bin/env python
# coding: utf-8

# In[2]:


# Import libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# In[5]:


# Load climate data from a CSV file
data = pd.read_csv('Marine_CSV_sample.csv')

# Data cleaning and preprocessing
# Remove rows with missing values
data.dropna(inplace = True)

# Convert Time of Observation to a datetime format
data['Time of Observation'] = pd.to_datetime(data['Time of Observation'])

# Select specific columns for analysis
selected_columns = ['Latitude', 'Longitude', 'Ice Accretion On Ship', 'Sea Level Pressure', 'Air Temperature', 'Sea Surface Temperature', 'Wave Height', 'Total Cloud Amount', 'Visibility', 'Wind Direction', 'Wind Speed']

# Extract the selected columns from the data
selected_data = data[selected_columns]

# Statistical analysis
# Calculate mean, median, and standard deviation for each selected column
statistics = selected_data.describe()

# Data visualization

plt.figure(figsize=(10, 6))
plt.scatter(selected_data['Air Temperature'], selected_data['Sea Surface Temperature'])
plt.title('Air Temperature vs. Sea Surface Temperature')
plt.xlabel('Air Temperature (°C)')
plt.ylabel('Sea Surface Temperature (°C)')
plt.grid(True)
plt.show()

plt.figure(figsize=(8, 5))
plt.hist(selected_data['Wind Speed'], bins=20, edgecolor='k')
plt.title('Wind Speed Histogram')
plt.xlabel('Wind Speed (m/s)')
plt.ylabel('Frequency')
plt.grid(True)
plt.show()

# Save the statistics to a CSV file
statistics.to_csv('climate_statistics.csv')

# Save the cleaned data to a new CSV file
selected_data.to_csv('cleaned_climate_data.csv', index=False)


# In[ ]:




