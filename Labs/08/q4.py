'''Task 4'''
'''Write a NumPy program to create a structured array from given student name, height, class and their data types. Now sort by class, then height if class are equal.'''

import numpy as np

dtype = [('name', 'U20'), ('height', 'f4'), ('class', 'i4')]
student = np.array([
    ('Alice', 5.7, 2),
    ('Maria', 5.4, 3),
    ('Charlie', 5.8, 2),
    ('David', 5.7, 1),
    ('Eve', 5.4, 2)
], dtype = dtype)

print(student)
data = np.sort(student, order = ['class', 'height'])
print("\nSorted: ")
print(data)