'''
 Programmer: Amna(23k-0066)
 Date: 28/Aug/2024
 Q1) Write a Python program to calculate the 
    • Area of a trapezoid 
    • Area of a parallelogram
    • Calculate surface volume and area of a cylinder.
'''


import math

def trapezoid(length, width, height):
    area = ((length + width) / 2) * height
    return area

def parallelogram(base, height):
    area = base * height
    return area

def cylinder(radius, height):
    volume = math.pi * radius * 2 * height
    area = (2 * radius * height * math.pi) + (2 * radius * radius * math.pi)
    print(f"Surface volume of cylinder is: {volume:.2f}")
    print(f"Area of cylinder is: {area:.2f}")


base1 = 5
base2 = 7
height_trapezoid = 4
trapezoid_area = trapezoid(base1, base2, height_trapezoid)
print(f"Area of the trapezoid: {trapezoid_area:.2f}")

base_parallelogram = 6
height_parallelogram = 5
parallelogram_area = parallelogram(base_parallelogram, height_parallelogram)
print(f"Area of the parallelogram: {parallelogram_area:.2f}")

radius_cylinder = 3
height_cylinder = 10
cylinder(radius_cylinder, height_cylinder)