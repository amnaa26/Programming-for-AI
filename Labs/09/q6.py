'''
Write a Python program to draw a scatter plot comparing two subject marks of Mathematics
and Science. Use marks of 10 students and also add legends for better understanding of the
data.
'''

import matplotlib.pyplot as plt

students = [f'Student {i+1}' for i in range(10)]
math_marks = [88, 92, 79, 85, 95, 70, 82, 90, 76, 89]  
science_marks = [75, 85, 80, 70, 90, 68, 78, 82, 88, 84]  

# Creating a scatter plot
plt.figure(figsize=(10, 6))
plt.scatter(students, math_marks, color='blue', label='Mathematics', marker='o')
plt.scatter(students, science_marks, color='green', label='Science', marker='s')
plt.title('Comparison of Mathematics and Science Marks')
plt.xlabel('Students')
plt.ylabel('Marks')
plt.xticks(rotation=45)  
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()
