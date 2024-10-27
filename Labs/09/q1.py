import matplotlib.pyplot as plt
import numpy as np

# data of 20 students
students = [f'Student {i+1}' for i in range(20)]
heights = np.random.randint(150, 190, size=20)  # Heights between 150 cm and 190 cm

# Bar chart
plt.figure(figsize=(10, 5))

# Create a bar chart
plt.subplot(1, 2, 1)  # 1=row, 2=columns, 1st subplot
colors = plt.cm.viridis(np.linspace(0, 1, len(students)))  # Different colors for each bar
plt.bar(students, heights, color=colors)
plt.title('Bar Chart of Student Heights')
plt.xlabel('Students')
plt.ylabel('Height (cm)')
plt.xticks(rotation=45)

# Pie chart
plt.subplot(1, 2, 2)  # 1 row, 2 columns, 2nd subplot
plt.pie(heights, labels=students, autopct='%1.1f%%', startangle=90)
plt.title('Pie Chart of Student Heights')

plt.tight_layout()
plt.show()
