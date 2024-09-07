
user = input("Enter a sentence: ")
filename = 'question.txt'

try:
    if user.strip().endswith('?'):
        with open(filename, 'a') as file:
            file.write(user + '\n')
        print("Question written to file successfully!..")
    else:
        print("Given sentence is not question, so not written to the file")
    

except FileNotFoundError:
    print("The file 'questions.txt' could not be found.")
except IOError:
    print("An error occurred while trying to write to the file.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
