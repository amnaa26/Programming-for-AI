'''
You have a list of cities and their respective populations. Create a horizontal bar graph to
visualize the populations of these cities.
'''

import matplotlib.pyplot as plt

cities = ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix', 'Philadelphia', 'San Antonio', 'San Diego', 'Dallas', 'San Jose']
populations = [8419600, 3980400, 2716000, 2328000, 1690000, 1584200, 1547200, 1423800, 1343000, 1027000]

# creating a horizontal bar graph
plt.figure(figsize=(10, 6))
plt.barh(cities, populations, color='skyblue')
plt.title('Population of Cities')
plt.xlabel('Population')
plt.ylabel('Cities')
plt.xlim(0, max(populations) + 1000000) 

plt.tight_layout()
plt.show()
