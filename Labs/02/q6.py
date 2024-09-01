# Programmer: Amna(23k-0066)
# Date: 28/Aug/2024
# Q6) Write a Python function to multiply all the numbers in a list.

def multiply_all_numbers(numbers):
    result = 1
    for number in numbers:
        result *= number

    return result



numbers_list = [2, 3, 4, 5]
product = multiply_all_numbers(numbers_list)
print("Product of all numbers:", product)