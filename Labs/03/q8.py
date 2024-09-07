'''
 Programmer: Amna(23k-0066)
 Date: 4/Sept/2024
 Q8) Take two integer numbers from user as input. Divide these two numbers. If one number is being divided by zero (another number) then handle ZeroDivisionError and if entered value
     is wrong (for example, a string) then handle ValueError.
'''

try:
    value1 = float(input("Enter value 1: "))
    value2 = float(input("Enter value 2: "))
    ans = value1/value2
    print(f"The result of {value1} divided by {value2} is: {ans:.2f}")

except ZeroDivisionError:
    print("Error: Division by zero is not allowed!")
    
except ValueError:
    print("Error: Please enter valid integer numbers!")
