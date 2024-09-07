'''
 Programmer: Amna(23k-0066)
 Date: 4/Sept/2024
 Q1) Write a Python program that reads a text file, counts the number of characters in it, andprints the total word count. Handle all possible exceptions as well.
 
'''


try:
    with open('text.txt', 'r') as text_file:
        content = text_file.read()
    total_chars = len(content)
    total_words = len(content.split())
    print("Total chars:", total_chars)
    print("Total words:", total_words)

except FileNotFoundError:
    print("File could not be found. \nEnding program...")
except IOError:
    print("An IOError occurred. \nEnding program...")
