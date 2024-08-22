# Programmer: Amna(23k-0066)
# Date: 21/Aug/2024
# Q6) Aliza has got 40 Marks in Physics, 78 in Chemistry and 82 in Maths. Take these marks as input from user and store them in dictionary with "key as subject name" and "value as marks". By accessing data stored in dictionary, print average of his marks and also print the name of subject in which she got highest marks.

value1 = float(input("Enter your marks in physics: "))
value2 = float(input("Enter your marks in chemistry: "))
value3 = float(input("Enter your marks in maths: "))
dictionary = {"Physics": value1, "Chemistry": value2, "Maths": value3}
highest = 0
avg = 0
for i in dictionary:
    if float(dictionary[i]) > highest:
        highest = float(dictionary[i])
    avg += float(dictionary[i])

print("\nHighest marks:", highest)
print("Average: ", avg/3)