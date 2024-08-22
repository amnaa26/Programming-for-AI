# Programmer: Amna(23k-0066)
# Date: 21/Aug/2024
# Q5) Write a program to take a list and a number input from user and then delete all elements in the list less than that number.

user = list(input("Enter an integer list: "))
number = int(input("Enter a number: "))
print("\nOriginal List: ", user)
filtered_list = []
for i in user:
    if number <= int(i):
        filtered_list.append(i)
print("\nList after the changes:", filtered_list)