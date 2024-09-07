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