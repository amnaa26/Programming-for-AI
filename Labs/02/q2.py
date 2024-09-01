# Programmer: Amna(23k-0066)
# Date: 28/Aug/2024
# Q2) Write a Python function to check if the last letter of user input string is a vowel or a consonant.

def check(number):
    alphabet = "aeiouAEIOU"
    if not number:
        print("String is empty")
    last_char = number[-1]
    if number.isalpha():
        i = 0
        while(i < len(alphabet)):
            if last_char == alphabet[i]:
                print("It is a vowel")
                break
            i += 1
    elif number.isdigit():
        print("The value of last character is not alphabetic")
    else:
        print("It is a constant")




user = input("Enter anything: ")
check(user)