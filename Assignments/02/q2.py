#Generate a 3x3 matrix with random integers. Calculate the transpose of the matrix.

import numpy as np

arr1 = np.random.randint(1, 101, size=(3, 3))
transpose = arr1.T

print("3x3 Matrix: \n", arr1)
print("\nTranspose: \n", transpose)