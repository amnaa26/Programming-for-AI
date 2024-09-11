'''
Programmer: Amna(23k-0066)
Date: 11/Sept/2024
Q4) Make a class "Employee". Create "get_data" function inside this class that will take input
    from user employee name ,monthly salary and percentage of tax. Create another function
    "Salary_after_tax" that will deduct 2% tax on monthly salary and return remaining salary.
    There will be another function of "update_tax_percentage" inside this class that will change
    tax percentage (for example initially if it was taken 2% then you may update it to 3%).
    Now again salary will be calculated based on this new tax percentage.
'''

class Employee:
    def __init__(self):
        self.name = ''
        self.monthly_salary = 0.0
        self.tax_percentage = 2.0

    def get_data(self):
        self.name = input("Enter Employee Name: ")
        self.monthly_salary = float(input("Enter Monthly Salary: "))
        self.tax_percentage = float(input("Enter Tax Percentage: "))

    def salary_after_tax(self):
        return self.monthly_salary - (self.monthly_salary * (self.tax_percentage / 100))

    def update_tax_percentage(self, new_tax_percentage):
        self.tax_percentage = new_tax_percentage


    def display(self):
        print(f"Employee Name: {self.name}")
        print(f"Monthly Salary (before tax): {self.monthly_salary}")
        print(f"Tax Percentage: {self.tax_percentage}%")
        print(f"Salary after tax: {self.salary_after_tax():.2f}")


# Main function
if __name__ == "__main__":
    emp = Employee()
    emp.get_data()
    emp.display()
    new_tax = float(input("\nEnter new tax percentage to update: "))
    emp.update_tax_percentage(new_tax)
    print("\nAfter updating the tax percentage:")
    emp.display()
