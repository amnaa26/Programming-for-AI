'''
You're interested in the gender distribution among the students in your dataset. Create a pie
chart to visualize the percentage of male and female students.
'''

import matplotlib.pyplot as plt

# Sample dataset of students with age and gender information
students_data = [
    {'name': 'Alice', 'age': 20, 'gender': 'Female'},
    {'name': 'Bob', 'age': 22, 'gender': 'Male'},
    {'name': 'Charlie', 'age': 19, 'gender': 'Male'},
    {'name': 'David', 'age': 21, 'gender': 'Male'},
    {'name': 'Eva', 'age': 23, 'gender': 'Female'},
    {'name': 'Frank', 'age': 24, 'gender': 'Male'},
    {'name': 'Grace', 'age': 22, 'gender': 'Female'},
    {'name': 'Hannah', 'age': 26, 'gender': 'Female'},
    {'name': 'Ian', 'age': 28, 'gender': 'Male'},
    {'name': 'Jasmine', 'age': 27, 'gender': 'Female'},
    {'name': 'Kevin', 'age': 25, 'gender': 'Male'},
    {'name': 'Laura', 'age': 29, 'gender': 'Female'},
    {'name': 'Mike', 'age': 30, 'gender': 'Male'},
    {'name': 'Nina', 'age': 31, 'gender': 'Female'},
    {'name': 'Oscar', 'age': 32, 'gender': 'Male'},
    {'name': 'Paul', 'age': 29, 'gender': 'Male'},
    {'name': 'Quinn', 'age': 24, 'gender': 'Female'},
    {'name': 'Rachel', 'age': 23, 'gender': 'Female'},
    {'name': 'Steve', 'age': 21, 'gender': 'Male'},
    #{'name': 'Tina', 'age': 22, 'gender': 'Female'},
]


# Counting genders
male_count = sum(1 for student in students_data if student['gender'] == 'Male')
female_count = sum(1 for student in students_data if student['gender'] == 'Female')

#data for pie chart
genders = ['Male', 'Female']
number_of_students = [male_count, female_count]

plt.figure(figsize=(8, 8))
plt.pie(number_of_students, labels=genders, autopct='%1.1f%%', startangle=90, colors=plt.cm.Set3.colors)
plt.title('Gender Distribution Among Students')
plt.axis('equal') 
plt.show()

