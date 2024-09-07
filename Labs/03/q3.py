'''
 Programmer: Amna(23k-0066)
 Date: 4/Sept/2024
 Q3) Write a python program that takes any two lists from user having same number of elements. Make a dictionary from these two lists in such a way that first element of first list will be key and first element of second list will be its associated value and so on. Store the dictionary in a text file. Handle all possible exceptions as well.
     Note: do not use any library. Make logic yourself.
'''

user_list1 = list(input("Enter values for list1: "))
user_list2 = list(input("Enter values for list2: "))

if len(user_list1) != len(user_list2):
    print("Number of values in both lists should be equal")

else:
    file_name = 'text.txt'
    dictionary = {}
    for i in range(len(user_list1)):
        key = user_list1[i]
        value = user_list2[i]
        dictionary[key] = value

    try:
        with open(file_name, 'a') as file:
            file.write(str(dictionary))
        with open(file_name, 'r') as file:
            file_content = file.read()
        print(file_content)

    except FileNotFoundError:
        print(f"The file '{file_name}' was not found.")
    except IOError as e:
        print(f"An IOError occurred: {e}")
