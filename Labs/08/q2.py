'''Task 2'''
'''Create a multi-dimensional array of 3 rows and 3 columns having odd numbers from 1 to 19 including 1 and excluding 19. After that, iterate over this array to print all elements.'''

import numpy as np
arr2 = np.arange(1,19,2).reshape(3,3)
print(arr2)
count = 1
for i in arr2:
    print(f"Element {count}: {i}")
    count = count + 1