'''
Define three lists, x, y1, and y2 and fill them with integers. These numbers can be anything
you want, but it would be neat to have them be actual metrics that you want to compare.
Plot y1 vs x and display the plot. On the same graph, plot y2 vs x (after the line where you
plot y1 vs x). Make the y1 line a pink line and the y2 line a gray line. Give both lines round
markers. Give your graph a title of your choice for example “Two Lines on One Graph”,
and label the x-axis” Amazing X-axis” and y-axis “Incredible Y-axis”. Give the graph a
legend and put it in the lower right.
'''

import matplotlib.pyplot as plt

# Define the data
x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]           # x-axis values (e.g., years or time intervals)
y1 = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]     # y1 values (e.g., prime numbers)
y2 = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]       # y2 values (e.g., Fibonacci numbers)

# creating plot
plt.figure(figsize=(10, 6))

# Plot y1 vs x
plt.plot(x, y1, color='pink', marker='o', label='Prime Numbers')
# Plot y2 vs x
plt.plot(x, y2, color='gray', marker='o', label='Fibonacci Numbers')

plt.title('Two Lines on One Graph')
plt.xlabel('Amazing X-axis')
plt.ylabel('Incredible Y-axis')

# Add legend in the lower right
plt.legend(loc='lower right')

# Show grid
plt.grid(True)

# Display the plot
plt.tight_layout()
plt.show()
