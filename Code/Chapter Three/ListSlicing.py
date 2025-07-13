# Write program to make use of list slicing concept to display elements of list.

# Initialize a list with some elements
my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90]

# Function to display elements of the list using slicing
def display_sliced_list(start, end):
    if start < 0 or end > len(my_list) or start >= end:
        print("Invalid slice range.")
    else:
        sliced_list = my_list[start:end]
        print(f"Sliced list from index {start} to {end}: {sliced_list}")

# Main program loop
while True:
    print("\nOptions:")
    print("1. Display full list")
    print("2. Display sliced list")
    print("3. Exit")
    
    choice = input("Enter your choice (1-3): ")
    
    if choice == '1':
        print("Full list:", my_list)
    elif choice == '2':
        start = int(input("Enter start index for slicing: "))
        end = int(input("Enter end index for slicing: "))
        display_sliced_list(start, end)
    elif choice == '3':
        print("Exiting the program.")
        break
    else:
        print("Invalid choice, please try again.")