'''Task 6'''
'''Write a NumPy program to multiply a 5x3 matrix by a 3x2.'''

import numpy as np
from numpy import random

arr = np.random.randint(100, size = (5, 3))
arr2 = np.random.randint(100, size = (3, 2))
arr3 = np.dot(arr, arr2)
print(arr3)