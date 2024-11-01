#Create a NumPy array with 50 random values. Find the indices of the maximum and minimum values in the array.

import numpy as np

arr1 = np.random.randint(1, 101, size=50)
maximum = np.argmax(arr1)
maximum_value = np.max(arr1)
minimum_value = np.min(arr1)
minimum = np.argmin(arr1)

print("Array: \n", arr1)
print(f"\nMaximum value {maximum_value} is found at index {maximum}")
print(f"Minimum value {minimum_value} is found at index {minimum}")