# Programmer: Amna(23k-0066)
# Date: 21/Aug/2024
# Q9) Write a Python program to create the multiplication table (from 1 to 10) of a number.

number = int(input("Enter a number and we will create a table for you: "))
i = 1
while i <= 10:
    print(number, " x ", i, " = ", number*i)
    i += 1