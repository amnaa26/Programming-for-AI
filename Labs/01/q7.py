# Programmer: Amna(23k-0066)
# Date: 21/Aug/2024
# Q7) Write a program that accepts a word from the user and reverses it using loop. For example, ‘Pakistan’ becomes‘natsikaP’.

user = input("Enter a word: ")
reversed_word = []
for i in range(len(user)-1, -1, -1): #range(start, stop, step)
    reversed_word.append(user[i])

reversed_str = ""
print("Orginal word: ", user)
print("Reversed word: ", reversed_str.join(reversed_word))
