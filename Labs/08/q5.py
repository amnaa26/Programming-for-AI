'''Task 5'''
'''Generate 4x4 matrix with random numbers only from (2,5,9,10) and then multiply this
matrix with identity matrix. Finally add this matrix to any 4x4 matrix having only odd
numbers.'''

import numpy as np
from numpy import random

x = random.choice([2, 5, 9, 10], size = (4,4))
print(x)
identity_matrix = np.identity(4)
x2 = np.dot(x, identity_matrix)
print(x2)
y = np.arange(1, 32, 2).reshape(4,4)
x3 = np.add(x2, y)
print(x3)