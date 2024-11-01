#Create a NumPy array with 20 values and reshape it into a 4x5 matrix.

import numpy as np

arr1 = np.random.randint(1, 101, size=20)
new_arr1 = arr1.reshape(4, 5)

print("Original Array: \n", arr1)
print("\nAfter reshaping: \n", new_arr1)