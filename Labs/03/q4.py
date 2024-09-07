'''
 Programmer: Amna(23k-0066)
 Date: 4/Sept/2024
 Q4) Take biodata of employee from user as Name, cnic number, age, and salary save it in txt file. Now append this file to add contact number. Finally read this file.
     Handle all possible exceptions as well.
'''

name = input("Enter your name: ")
cnic_number = input("Enter your CNIC number: ")
age = input("Enter your age: ")
salary = input("Enter your salary: ")
contact_no = input("Enter your contact number: ")
file_name = 'sample.txt'

try:
    with open(file_name, 'w') as file:
        file.write(f"Name: {name}\n")
        file.write(f"CNIC Number: {cnic_number}\n")
        file.write(f"Age: {age}\n")
        file.write(f"Salary: {salary}\n")
    with open(file_name, 'a') as file:
        file.write(f"Contact number: {contact_no}\n")
    print("Successfully written all the information in the file\n")

except FileNotFoundError:
    print(f"The file '{file_name}' was not found.")
except IOError as e:
    print(f"An IOError occurred: {e}")

