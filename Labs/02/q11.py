'''
Programmer: Amna(23k-0066)
Date: 28/Aug/2024
Q11) You have a dictionary where each key is a student's name and each value is a list of their grades. You need to perform the following operations:
    • Add a new grade to a student's list of grades.
    • Calculate and print the average grade for a specific student.
    • Add a new student with an initial empty list of grades.
    • Remove a student from the dictionary
'''

def add_grade(students_dict, student_name, grade):
    if student_name in students_dict:
        students_dict[student_name].append(grade)
        print(f"Added grade {grade} for {student_name}.")
    else:
        print(f"Student {student_name} not found.")

def calculate_avg(students_dict, student_name):
    if student_name in students_dict:
        grades = students_dict[student_name]
        if grades:
            average = sum(grades)/len(grades)
            print(f"Average grade for {student_name} is {average:.2f}.")
        else:
            print(f"{student_name} has no grades.")
    else:
        print(f"Student {student_name} not found.")

def add_student(students_dict, student_name):
    if student_name not in students_dict:
        students_dict[student_name] = []
        print(f"Student {student_name} added.")
    else:
        print(f"Student {student_name} already exits.")

def remove_student(students_dict, student_name):
    if student_name in students_dict:
        del students_dict[student_name]
        print(f"student {student_name} removed.")
    else:
        print(f"Student {student_name} does not exists.")


students = {
    "Alice": [78, 25, 67, 89],
    "Bob": [34, 89, 90, 35],
    "David": [67, 89, 56, 45],
    "Charlie": [89, 76, 77, 90]
}

print(students)
print("\n")
add_grade(students, "Bob", 78)
calculate_avg(students, "Alice")
add_student(students, "Flora")
add_student(students, "Charlie")
remove_student(students, "David")
remove_student(students, "ABC")

print("\nDictionary after the changes: ")
print(students)