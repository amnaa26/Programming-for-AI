# Programmer: Amna(23k-0066)
# Date: 21/Aug/2024
# Q7) Write a program that accepts a word from the user and reverses it using loop. For example, ‘Pakistan’ becomes‘natsikaP’.

user = input("Enter a word: ")
reversed_word = user[::-1] #string[beginning:end:step] -> string slicing
print("Original word: ", user)
print("Reversed word: ", reversed_word)