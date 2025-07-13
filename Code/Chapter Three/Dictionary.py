# Write program to create dictionary, add elements in dictionary, remove elements from dictionary and display dictionary items.

# Initialize an empty dictionary
my_dict = {}

# Function to display the dictionary
def display_dict():
    if not my_dict:
        print("The dictionary is empty.")
    else:
        print("Current dictionary items:")
        for key, value in my_dict.items():
            print(f"{key}: {value}")

# Function to add an item to the dictionary
def add_item(key, value):
    my_dict[key] = value
    print(f"Item '{key}: {value}' added to the dictionary.")

# Function to remove an item from the dictionary
def remove_item(key):
    if key in my_dict:
        del my_dict[key]
        print(f"Item '{key}' removed from the dictionary.")
    else:
        print(f"Key '{key}' not found in the dictionary.")

# Function to clear the dictionary
def clear_dict():
    my_dict.clear()
    print("The dictionary has been cleared.")

# Main program loop

while True:
    print("\nOptions:")
    print("1. Display dictionary")
    print("2. Add item to dictionary")
    print("3. Remove item from dictionary")
    print("4. Clear dictionary")
    print("5. Exit")
    
    choice = input("Enter your choice (1-5): ")
    
    if choice == '1':
        display_dict()
    elif choice == '2':
        key = input("Enter the key: ")
        value = input("Enter the value: ")
        add_item(key, value)
    elif choice == '3':
        key = input("Enter the key to remove: ")
        remove_item(key)
    elif choice == '4':
        clear_dict()
    elif choice == '5':
        print("Exiting the program.")
        break
    else:
        print("Invalid choice, please try again.")

        



