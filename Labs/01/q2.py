# Programmer: Amna(23k-0066)
# Date: 21/Aug/2024
# Q2) Write a program to make a simple calculator performing the four basic operations (+, -, *, /) on two numbers input by user. The following conditionsmustbe satisfied:
#     a) A ‘+’ sign must not be used foraddition.
#     b) You can only use a maximum of 3 variables. No more variables are allowed.
#     c) Your program should ask the user which operation he/she wants to perform and gives the output accordingly.

var1 = int(input("Enter variable: "))
var2 = int(input("Enter variable2: "))
choice = input("Enter operator: ")

if choice == '+':
    var3 = -(-var1 - var2)
elif choice == '-':
    var3 = var2 - var1
elif choice == '*':
    var3 = var2 * var1
else:
    var3 = var2 / var1

print(var3)