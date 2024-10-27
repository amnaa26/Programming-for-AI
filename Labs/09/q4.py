'''
Create a pie chart to show the distribution of student ages by dividing them into groups (e.g.,
18-25, 26-30, 31-35, 36 and above). Use the provided dataset for data.
'''

import matplotlib.pyplot as plt
import numpy as np

ages = [18, 19, 21, 22, 24, 25, 26, 27, 29, 30, 31, 33, 34, 35, 36, 38, 40, 41, 42, 50]
age_groups = ['18-25', '26-30', '31-35', '36 and above']
age_distribution = [0] * len(age_groups)  # Initialize count for each group

# Counting the number of students in each age group
for age in ages:
    if 18 <= age <= 25:
        age_distribution[0] += 1
    elif 26 <= age <= 30:
        age_distribution[1] += 1
    elif 31 <= age <= 35:
        age_distribution[2] += 1
    elif age >= 36:
        age_distribution[3] += 1

plt.figure(figsize=(8, 8))
plt.pie(age_distribution, labels=age_groups, autopct='%1.1f%%', startangle=90, colors=plt.cm.Paired.colors)
plt.title('Distribution of Student Ages')
plt.axis('equal') 
plt.show()
