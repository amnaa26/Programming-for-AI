#Create a 3x3 matrix representing a system of linear equations. Use NumPy to solve the system and print the solution.

import numpy as np

coefficient_matrix = np.random.randint(1, 10, size=(3, 3))
constant_vector = np.random.randint(1, 10, size=3)
output = np.linalg.solve(coefficient_matrix, constant_vector)

print("Coefficient Matrix: \n", coefficient_matrix)
print("Constant Vector: \n", constant_vector)
print("\nSolution of the system: \n", np.round(output, 1))