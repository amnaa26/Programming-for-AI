#Create a one-dimensional NumPy array containing integers from 1 to 10. Compute the sum, mean, and product of the array.

import numpy as np

arr1 = np.arange(1, 11)
sum_of_arr1 = np.sum(arr1)
mean_of_arr1 = np.mean(arr1)
product_of_arr1 = np.prod(arr1)

print("Array: ", arr1)
print("Sum:", sum_of_arr1)
print("Mean:", mean_of_arr1)
print("Product:", product_of_arr1)
