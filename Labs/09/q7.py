'''
Write a Python program to draw a scatter plot to find sea level rise in past 100 years. Use the
provided dataset.
'''

import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('epa-sea-level.csv')
years = data['Year']
sea_levels = data['CSIRO Adjusted Sea Level']

# Creating a scatter plot
plt.figure(figsize=(10, 6))
plt.scatter(years, sea_levels, color='blue', marker='o', label='Sea Level Rise')
plt.title('Sea Level Rise Over the Past 100 Years')
plt.xlabel('Year')
plt.ylabel('Sea Level (meters)')
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()
