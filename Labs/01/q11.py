# Programmer: Amna(23k-0066)
# Date: 21/Aug/2024
# Q11) Write a program to take marks of 3 subjects as input by user and store them in a dictionary having appropriate keys. Using that dictionary calculate average and percentage of those marks.

user = input("Enter your marks of any 3 subjects separated by a comma: ")
user = user.split(",")
dictionary = {}
index = 1
for index in range(len(user)):
    key = "Subject" + str(index + 1)
    dictionary[key] = int(user[index])

obtained = 0
for i in dictionary:
    obtained += dictionary[i]

avg = obtained / len(dictionary)

#Lets assume that the total marks are 300
percentage = (obtained/(100*len(dictionary))) * 100

print("Marks Dictionary: ", dictionary)
print("Total marks obtained: ", obtained)
print("Average: {:.2f}".format(avg))
print("Percentage: {:.2f}%".format(percentage))
