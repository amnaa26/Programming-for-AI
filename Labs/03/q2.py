def replace_word(file_name, old_word, new_word):
    try:
        with open(file_name, 'r') as file:
            file_content = file.read()
        updated_content = file_content.replace(old_word, new_word)
        with open(file_name, 'w') as file:
            file.write(updated_content)


    except FileNotFoundError:
        print(f"The file '{file_name}' was not found.")
    except IOError as e:
        print(f"An IOError occurred: {e}")


file_name = 'text.txt'
old_word = 'JSON'
new_word = 'JavaScript Object Notation'
replace_word(file_name, old_word, new_word)
with open(file_name, 'r') as file:
    file_content = file.read()
print(file_content)


