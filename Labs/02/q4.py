# Programmer: Amna(23k-0066)
# Date: 28/Aug/2024
# Q4) Write a program to make function employee() meeting following requirements: Employee name and monthly salary will be passed to this function. This function will cut 2 percent tax from salary and display salary after tax with name of employee. If the salary is missing in the function call then assign default value 10,000 to salary.

def employee(name, salary = 10000):
    tax_deduction = 0.2 * salary
    new_salary = salary - tax_deduction
    print("Name: ", name)
    print("Salary before deduction: ", salary)
    print("Salary after deduction: ", new_salary)


employee("Amna", 450000)
employee("abc")