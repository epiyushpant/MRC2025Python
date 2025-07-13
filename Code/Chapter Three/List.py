#Write program to create list, add elements in list, remove elements from list and display list items.

# Initialize an empty list
my_list = []
# Function to display the list
def display_list():
    if not my_list:
        print("The list is empty.")
    else:
        print("Current list items:")
        for item in my_list:
            print(item)

# Function to add an item to the list
def add_item(item):
    my_list.append(item)
    print(f"Item '{item}' added to the list.")
    
# Function to remove an item from the list
def remove_item(item):
    if item in my_list:
        my_list.remove(item)
        print(f"Item '{item}' removed from the list.")
    else:
        print(f"Item '{item}' not found in the list.")

# Main program loop
while True:
    print("\nOptions:")
    print("1. Display list")
    print("2. Add item to list")
    print("3. Remove item from list")
    print("4. Exit")
    
    choice = input("Enter your choice (1-4): ")
    
    if choice == '1':
        display_list()
    elif choice == '2':
        item = input("Enter the item to add: ")
        add_item(item)
    elif choice == '3':
        item = input("Enter the item to remove: ")
        remove_item(item)
    elif choice == '4':
        print("Exiting the program.")
        break
    else:
        print("Invalid choice, please try again.")

