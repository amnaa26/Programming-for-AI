'''
Programmer: Amna(23k-0066)
Date: 11/Sept/2024
Q3) Make a class "Student" and make a function "Print_biodata" inside it. Pass name and age of
    student to constructor. Now access "Print_biodata" function using object to print name and
    age of student.
'''

class Student:
    # Constructor
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def Print_biodata(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")

#object of class Student
student1 = Student("John Doe", 20)
student1.Print_biodata()
