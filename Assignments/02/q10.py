#Implement a function that accepts a NumPy array and normalizes it (subtracts the mean and divides by the standard deviation). Apply this function to a sample array.

import numpy as np

def normalize_array(arr1):
    mean_value = np.mean(arr1)
    standard_deviation = np.std(arr1)
    result = (arr1 - mean_value) / standard_deviation
    return result

arr1 = np.random.randint(1, 51, size=10)
normalize_arr1 = normalize_array(arr1)
print("Original Array: \n", arr1)
print("\nNormalized Array: \n", normalize_arr1)

