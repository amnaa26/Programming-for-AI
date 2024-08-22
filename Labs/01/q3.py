# Programmer: Amna(23k-0066)
# Date: 21/Aug/2024
# Q3) Write a program to take an integerlist inputfrom user and count all the even numbers in that list and print the count.

user = list(input("Enter integer list: "))
print(user)
count = 0
for i in user:
    check = int(i) % 2
    if check == 0:
        count = count + 1

print(count)