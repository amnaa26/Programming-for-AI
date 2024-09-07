import json

dictionary = {}
file_name = 'sample2.txt'

while True:
    name = input("Enter name (enter exit if you want to leave): ").strip()
    if name == 'exit':
        break
    else:
        age = input("Enter age: ").strip()
        if not age.isdigit():
            print("Invalid age. Please enter a numeric value.")
            continue
        dictionary[name] = age

try:
    with open(file_name, 'w') as file:
        json.dump(dictionary, file, indent = 4)
    print(f"Data successfully saved to {file_name}.")
    with open(file_name, 'r') as file:
        data = json.load(file)
    print("Data successfully loaded from the JSON file:")
    print(data)
    max_value = max(data.values())
    max_key = max(data, key=data.get)  # Get the key for the maximum value
    print(f"'{max_key}' has the maximum age of '{max_value}'.")
    age_count = {}
    for age in dictionary.values():
        if age in age_count:
            age_count[age] += 1
        else:
            age_count[age] = 1

    duplicates_found = False
    for age, count in age_count.items():
        if count > 1:
            duplicates_found = True
            names_with_age = [name for name, person_age in dictionary.items() if person_age == age]
            print(f"Age {age} is shared by {count} person(s): {', '.join(names_with_age)}")

        if not duplicates_found:
            print("No duplicate ages found.")

except FileNotFoundError:
    print(f"File '{file_name}' not found.")
except json.JSONDecodeError:
    print(f"Error decoding JSON in file '{file_name}'.")
except IOError as e:
    print(f"An IOError occurred: {e}")