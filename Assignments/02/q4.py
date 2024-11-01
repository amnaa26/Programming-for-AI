#Perform element-wise addition, subtraction, multiplication, and division on two NumPy arrays of your choice

import numpy as np

arr1 = np.random.randint(1, 101, size=10)
arr2 = np.random.randint(1, 101, size=10)
division = np.divide(arr1, arr2)

print("Array 1: ", arr1)
print("Array 2: ", arr2)
print("\n\nAddition: ", np.add(arr1, arr2))
print("Subtraction: ", np.subtract(arr1, arr2))
print("Multiplication: ", np.multiply(arr1, arr2))
print("Division: ", np.round(division , 2)) #rounds upto 2 decimal point