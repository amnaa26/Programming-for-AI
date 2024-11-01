#Generate a 2x2 matrix and calculate its determinant and inverse.

import numpy as np

arr1 = np.random.randint(1, 101, size=(2, 2))
determinant = np.linalg.det(arr1)

print("Matrix 2x2: \n", arr1)

if determinant != 0:
    inverse = np.linalg.inv(arr1)
    print("\nDeterminant: ", np.round(determinant, 2))
    print("Inverse: \n", np.round(inverse, 2))

else:
    print("Determinant: ", np.round(determinant, 2))
    print("Inverse does not exists as it it's determinant is zero")


