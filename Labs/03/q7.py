def correct_file_content(wrong_char, correct_char):
    try:
        with open("replacement_needed.txt", "r") as file:
            content = file.read()
        print("Original content:", content)

        corrected_content = content.replace(wrong_char, correct_char)
        print("Corrected content:", corrected_content)

        with open("replacement_needed.txt", "w") as file:
            file.write(corrected_content)
        print("The content has been corrected and saved.")


    except FileNotFoundError:
        print("The file 'replacement_needed.txt' could not be found.")
    except IOError:
        print("An error occurred while reading or writing to the file.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


wrong_char = input("Enter the wrong character in the text: ")
correct_char = input("Enter the correct character to replace it with: ")
correct_file_content(wrong_char, correct_char)
