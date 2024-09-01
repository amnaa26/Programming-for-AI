# Programmer: Amna(23k-0066)
# Date: 28/Aug/2024
# Q5) Write a function that will take a number 'n' input by user and will return its factorial.

def factorial(n):
    if n < 0:
        print("Factorial is not defined for negative numbers.")
    elif n == 0 or n == 1:
        return 1
    else:
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result



print("Factorial of 2 is:", factorial(2))
print("Factorial of 8 is:", factorial(8))
print("Factorial of 1 is:", factorial(1))
factorial(-1)