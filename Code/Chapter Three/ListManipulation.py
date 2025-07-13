# Write program to elaborate different list methods.

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

# Function to clear the list
def clear_list():
    my_list.clear()
    print("The list has been cleared.")

# Function to sort the list
def sort_list():
    if my_list:
        my_list.sort()
        print("The list has been sorted.")
    else:
        print("The list is empty, nothing to sort.")

# Function to reverse the list
def reverse_list():
    if my_list:
        my_list.reverse()
        print("The list has been reversed.")
    else:
        print("The list is empty, nothing to reverse.")
# Function to count occurrences of an item
def count_item(item):
    count = my_list.count(item)
    print(f"Item '{item}' occurs {count} time(s) in the list.")

# Main program loop
while True:
    print("\nOptions:")
    print("1. Display list")
    print("2. Add item to list")
    print("3. Remove item from list")
    print("4. Clear list")
    print("5. Sort list")
    print("6. Reverse list")
    print("7. Count occurrences of an item")
    print("8. Exit")
    
    choice = input("Enter your choice (1-8): ")
    
    if choice == '1':
        display_list()
    elif choice == '2':
        item = input("Enter the item to add: ")
        add_item(item)
    elif choice == '3':
        item = input("Enter the item to remove: ")
        remove_item(item)
    elif choice == '4':
        clear_list()
    elif choice == '5':
        sort_list()
    elif choice == '6':
        reverse_list()
    elif choice == '7':
        item = input("Enter the item to count: ")
        count_item(item)
    elif choice == '8':
        print("Exiting the program.")
        break
    else:
        print("Invalid choice, please try again.")

# This code demonstrates various list methods in Python, including adding, removing, clearing, sorting, reversing, and counting items in a list.



