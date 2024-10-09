'''Task 3'''
'''Create 3x3 matrix containing only even numbers. Multiply each element of this array with 4 and then multiply resultant matrix with 3x3 identity matrix (identity matrix should not be hardcoded).'''
import numpy as np
arr3 = np.arange(2, 20, 2).reshape(3,3)
print(arr3)
arr3 = np.dot(arr3, 4)
print(arr3)
identity_matrix = np.eye(3, 3)
arr3 = np.dot(arr3, identity_matrix)
print(arr3)