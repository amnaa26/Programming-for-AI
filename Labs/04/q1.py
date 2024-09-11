'''
Programmer: Amna(23k-0066)
Date: 11/Sept/2024
Q1) Suppose a = ["He", "th", "i", "sal"] and b = ["llo", "is", "s", "man"]
    You need to print this : ['Hello', 'this', 'is', 'salman']
    After attempting this question, make sure you may also write this query in one line.
'''


a = ["He", "th", "i", "sal"]
b = ["llo", "is", "s", "man"]
c = []
for i, j in zip(a, b):
    c.append(i + j)
print(c)


#one-liner solution
result = [i + j for i, j in zip(a, b)]
print(result)

