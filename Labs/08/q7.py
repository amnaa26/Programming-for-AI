'''Task 7'''
'''Write a NumPy program to create a random array with 1000 elements and compute the
average, variance, standard deviation of the array elements. Save all the results in text file
created at runtime.'''

import numpy as np
from numpy import random

arr = np.random.randint(1000, size=(4,4))
avg = np.average(arr)
variance = np.var(arr)
deviation = np.std(arr)

results = f"Average: {avg}\nVariance: {variance}\nStandard Deviation: {deviation}"
filename = "random_array_statistics.txt"
with open(filename, "w") as file:
    file.write(results)

print(f"Results saved to {filename}")
