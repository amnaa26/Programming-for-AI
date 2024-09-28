#Programmer: Amna(23k-0066)
#Date: 18th Sept 2024

class Student:
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def display(self):
        print("Student name: ", self.name)
        print("Student ID: ", self.id)


class Marks(Student):
    def __init__(self, name, id, marks_algo, marks_datascience, marks_calculus):
        super().__init__(name, id)
        self.marks_algo = marks_algo
        self.marks_datascience = marks_datascience
        self.marks_calculus = marks_calculus

    def display_marks(self):
        print("Displaying obtained marks of courses: ")
        print("Algorithms: ", self.marks_algo)
        print("Data science: ", self.marks_datascience)
        print("Calculus: ", self.marks_calculus)


class Result(Marks):
    def __init__(self, name, id, marks_algo, marks_datascience, marks_calculus):
        super().__init__(name, id, marks_algo, marks_datascience, marks_calculus)

    def display_result(self):
        self.total = self.marks_calculus + self.marks_algo + self.marks_datascience
        self.average = self.total / 3
        print("Total marks obtained: ", self.total)
        print("Average marks obtained: ", self.average)



a = Result("Alice", "24k-0987", 67, 89, 78)
a.display()
a.display_marks()
a.display_result()
