#Create a NumPy array of 10 values and apply the square root function to each element.

import numpy as np

arr1 = np.random.randint(1, 101, size=10)
#arr1 = np.arange(1, 11)
sqrt_arr1 = np.sqrt(arr1)

print("Original Array: ", arr1)
print("After square root: ", np.round(sqrt_arr1, 2))