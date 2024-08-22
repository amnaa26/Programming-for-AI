# Programmer: Amna(23k-0066)
# Date: 21/Aug/2024
# Q12) Write a program to print a dictionary where the keys are numbers between 1 and 15 (both included) and the values are the square of the keys.

dictionary = {}
i = 1
while i <= 15:
    dictionary[i] = i ** 2
    i += 1

print(dictionary)