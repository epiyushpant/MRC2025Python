#Write program to create set, add elements in set, remove elements from set and display set items.

# Initialize an empty set
my_set = set()
# Function to display the set
def display_set():  
    if not my_set:
        print("The set is empty.")
    else:
        print("Current set items:")
        for item in my_set:
            print(item)


# Function to add an item to the set
def add_item(item):
    my_set.add(item)
    print(f"Item '{item}' added to the set.")   

# Function to remove an item from the set
def remove_item(item):
    if item in my_set:
        my_set.remove(item)
        print(f"Item '{item}' removed from the set.")
    else:
        print(f"Item '{item}' not found in the set.")

# Main program loop
while True:
    print("\nOptions:")
    print("1. Display set")
    print("2. Add item to set")
    print("3. Remove item from set")
    print("4. Exit")
    
    choice = input("Enter your choice (1-4): ")
    
    if choice == '1':
        display_set()
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