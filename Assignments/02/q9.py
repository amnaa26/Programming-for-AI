#Create a NumPy array with 25 values and calculate the 75th percentile.

import numpy as np

#arr1 = np.random.rand(25) can also be used for generating 25 pseudorandom values
arr1 = np.random.randint(1, 51, size=25)
print("Array: \n", arr1)
print("75th Percentile: ", np.percentile(arr1, 75))