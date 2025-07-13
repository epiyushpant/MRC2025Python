#Write program to perform set operations.

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

# Function to perform union of two sets
def union_sets(other_set):
    union_result = my_set.union(other_set)
    print("Union of sets:")
    print(union_result)

# Function to perform intersection of two sets
def intersection_sets(other_set):
    intersection_result = my_set.intersection(other_set)
    print("Intersection of sets:")
    print(intersection_result)
# Function to perform difference of two sets    

def difference_sets(other_set):
    difference_result = my_set.difference(other_set)
    print("Difference of sets:")
    print(difference_result)            

# Function to perform symmetric difference of two sets
def symmetric_difference_sets(other_set):
    symmetric_difference_result = my_set.symmetric_difference(other_set)
    print("Symmetric difference of sets:")
    print(symmetric_difference_result)

# Main program loop
while True:
    print("\nOptions:")
    print("1. Display set")
    print("2. Add item to set")
    print("3. Remove item from set")
    print("4. Union with another set")
    print("5. Intersection with another set")
    print("6. Difference with another set")
    print("7. Symmetric difference with another set")
    print("8. Exit")

    choice = input("Enter your choice (1-8): ")

    if choice == '1':
        display_set()
    elif choice == '2':
        item = input("Enter the item to add: ")
        add_item(item)
    elif choice == '3':
        item = input("Enter the item to remove: ")
        remove_item(item)
    elif choice == '4':
        other_set = set(input("Enter items for the other set (comma separated): ").split(","))
        union_sets(other_set)
    elif choice == '5':
        other_set = set(input("Enter items for the other set (comma separated): ").split(","))
        intersection_sets(other_set)
    elif choice == '6':
        other_set = set(input("Enter items for the other set (comma separated): ").split(","))
        difference_sets(other_set)
    elif choice == '7':
        other_set = set(input("Enter items for the other set (comma separated): ").split(","))
        symmetric_difference_sets(other_set)
    elif choice == '8':
        print("Exiting the program.")
        break
    else:
        print("Invalid choice, please try again.")

        