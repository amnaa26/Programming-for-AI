#Write a Pandas program to import excel data (employee.xlsx ) into a Pandas dataframe and find a list of employees of a specified year.

import pandas as pd

data = pd.read_excel("employee_data.xlsx")

specified_year = 1997
data['Date Hired'] = pd.to_datetime(data['Date Hired'], format='%d/%m/%Y')
data['Year'] = data['Date Hired'].dt.year

filtered_employees = data[data['Year'] == specified_year]
print(f"\nEmployees in the year {specified_year}:")
print(filtered_employees)

specified_year = 2008
filtered_employees2 = data[data['Year'] == specified_year]
print(f"\nEmployees in the year {specified_year}:")
print(filtered_employees2)