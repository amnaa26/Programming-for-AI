'''
You have a list of ice cream flavors and the number of scoops sold for each flavor. Create a pie
chart to show the distribution of ice cream sales.
'''

import matplotlib.pyplot as plt

flavors = ['Vanilla', 'Chocolate', 'Strawberry', 'Mint', 'Cookies & Cream', 'Rocky Road', 'Pistachio', 'Mango', 'Matcha', 'Coffee']
scoops_sold = [150, 120, 90, 80, 110, 70, 60, 50, 40, 30]

# creating pie chart
plt.figure(figsize=(8, 8))
plt.pie(scoops_sold, labels=flavors, autopct='%1.1f%%', startangle=90, colors=plt.cm.tab10.colors)
plt.title('Distribution of Ice Cream Sales by Flavor')
plt.axis('equal')  
plt.show()
