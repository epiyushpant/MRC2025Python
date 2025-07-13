# Write program to make use of string manipulation methods and also perform different string operations.

# Initialize an empty string
my_string = ""
# Function to display the string
def display_string():
    if not my_string:
        print("The string is empty.")
    else:
        print("Current string:")
        print(my_string)

# Function to add a substring to the string
def add_substring(substring):
    global my_string
    my_string += substring
    print(f"Substring '{substring}' added to the string.")

# Function to remove a substring from the string
def remove_substring(substring):
    global my_string
    if substring in my_string:
        my_string = my_string.replace(substring, "", 1)
        print(f"Substring '{substring}' removed from the string.")
    else:
        print(f"Substring '{substring}' not found in the string.")

# Function to clear the string

def clear_string():
    global my_string
    my_string = ""
    print("The string has been cleared.")       

# Function to count occurrences of a substring
def count_substring(substring):
    count = my_string.count(substring)
    print(f"Substring '{substring}' occurs {count} time(s) in the string.")

# Function to find the index of a substring
def find_substring(substring):
    index = my_string.find(substring)
    if index != -1:
        print(f"Substring '{substring}' found at index {index}.")
    else:
        print(f"Substring '{substring}' not found in the string.")

# Function to replace a substring with another substring
def replace_substring(old_substring, new_substring):
    global my_string
    if old_substring in my_string:
        my_string = my_string.replace(old_substring, new_substring)
        print(f"Substring '{old_substring}' replaced with '{new_substring}'.")
    else:
        print(f"Substring '{old_substring}' not found in the string.")

# Main program loop
while True:
    print("\nOptions:")
    print("1. Display string")
    print("2. Add substring to string")
    print("3. Remove substring from string")
    print("4. Clear string")
    print("5. Count occurrences of a substring")
    print("6. Find index of a substring")
    print("7. Replace a substring with another substring")
    print("8. Exit")
    
    choice = input("Enter your choice (1-8): ")
    
    if choice == '1':
        display_string()
    elif choice == '2':
        substring = input("Enter the substring to add: ")
        add_substring(substring)
    elif choice == '3':
        substring = input("Enter the substring to remove: ")
        remove_substring(substring)
    elif choice == '4':
        clear_string()
    elif choice == '5':
        substring = input("Enter the substring to count: ")
        count_substring(substring)
    elif choice == '6':
        substring = input("Enter the substring to find: ")
        find_substring(substring)
    elif choice == '7':
        old_substring = input("Enter the old substring: ")
        new_substring = input("Enter the new substring: ")
        replace_substring(old_substring, new_substring)
    elif choice == '8':
        print("Exiting the program.")
        break
    else:
        print("Invalid choice, please try again.")


