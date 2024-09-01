# Programmer: Amna(23k-0066)
# Date: 28/Aug/2024
# Q9) Write a Python program that reads a text file, counts the number of characters in it, and prints the total word count.

text_file = open('text.txt')
for i in text_file:
    content = i

total_chars = len(content)
total_words = len(content.split(' '))
print("Total chars: ", total_chars)
print("Total words: ", total_words)
