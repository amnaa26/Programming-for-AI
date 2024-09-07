try:
    value1 = float(input("Enter value 1: "))
    value2 = float(input("Enter value 2: "))
    ans = value1/value2
    print(f"The result of {value1} divided by {value2} is: {ans:.2f}")

except ZeroDivisionError:
    print("Error: Division by zero is not allowed!")
    
except ValueError:
    print("Error: Please enter valid integer numbers!")