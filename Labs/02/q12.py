# Programmer: Amna(23k-0066)
# Date: 28/Aug/2024
# Q12) Write a python program that takes any two lists from user having same number of elements. Make a dictionary from these two lists in such a way that first element of first list will be key and first element of second list will be its associated value and so on and print the result.
#      Note: do not use any library. Make logic yourself.

user_list1 = list(input("Enter values for list1: "))
user_list2 = list(input("Enter values for list2: "))

if len(user_list1) != len(user_list2):
    print("Number of values in both lists should be equal")

else:
    dictionary = {}
    for i in range(len(user_list1)):
        key = user_list1[i]
        value = user_list2[i]
        dictionary[key] = value

    print(dictionary)
