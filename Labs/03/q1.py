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