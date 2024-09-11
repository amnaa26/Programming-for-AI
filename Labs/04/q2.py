'''
Programmer: Amna(23k-0066)
Date: 11/Sept/2024
Q2) Two lists are given : list1 = ["Hello ", "take "] , list2 = ["Dear", "Sir"]
    Concatenate these two lists like this : ['Hello Dear', 'Hello Sir', 'take Dear', 'take Sir']
'''

a = ["Hello ", "take "]
b = ["Dear", "Sir"]
c = []
for i in a:
    for j in b:
        c.append(i + j)
print(c) 