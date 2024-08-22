# Programmer: Amna(23k-0066)
# Date: 21/Aug/2024
# Q4) Write a program that takes a list of numbers as input and returns the sum of all the elements in the list.

user = list(input("Enter integer list: "))
print(user)
count = 0
for i in user:
    count += int(i)

print(count)