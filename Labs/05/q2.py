#Programmer: Amna(23k-0066)
#Date: 18th Sept 2024

from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def calculate_area(self):
        pass

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calculate_area(self):
        self.area = self.length * self.width
        print("Area of rectangle is: ",self.area)


class Triangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        self.area = 0.5 * self.width * self.height
        print("Area of triangle is: ", self.area)


class Square(Shape):
    def __init__(self, side):
        self.side = side

    def calculate_area(self):
        self.area = self.side * self.side
        print("Area of square is: ", self.area)



a = Rectangle(20, 12)
a.calculate_area()
b = Square(5)
b.calculate_area()
c = Triangle(12, 20)
c.calculate_area()