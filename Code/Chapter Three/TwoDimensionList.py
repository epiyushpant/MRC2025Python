# Write program to illustrate two-dimensional list.
two_d_list = [
    [1, 2, 3],          
    [4, 5, 6],
    [7, 8, 9]
]

# Function to display the 2D list
def display_2d_list():
    print("Current 2D list:")
    for row in two_d_list:
        print(row)  

# Function to add a new row to the 2D list
def add_row(row):
    two_d_list.append(row)
    print(f"Row {row} added to the 2D list.")

# Function to remove a row from the 2D list
def remove_row(index):
    if 0 <= index < len(two_d_list):
        removed_row = two_d_list.pop(index)
        print(f"Row {removed_row} removed from the 2D list.")
    else:
        print("Invalid index, cannot remove row.")

# Function to clear the 2D list
def clear_2d_list():
    two_d_list.clear()
    print("The 2D list has been cleared.")

# Function to transpose the 2D list
def transpose_2d_list():
    transposed = [[two_d_list[j][i] for j in range(len(two_d_list))] for i in range(len(two_d_list[0]))]
    print("Transposed 2D list:")
    for row in transposed:
        print(row)
    

# Main program loop
while True:
    print("\nOptions:")
    print("1. Display 2D list")
    print("2. Add row to 2D list")
    print("3. Remove row from 2D list")
    print("4. Clear 2D list")
    print("5. Transpose 2D list")
    print("6. Exit")
    
    choice = input("Enter your choice (1-6): ")
    
    if choice == '1':
        display_2d_list()
    elif choice == '2':
        row = list(map(int, input("Enter the new row elements separated by space: ").split()))
        add_row(row)
    elif choice == '3':
        index = int(input("Enter the index of the row to remove: "))
        remove_row(index)
    elif choice == '4':
        clear_2d_list()
    elif choice == '5':
        transpose_2d_list()
    elif choice == '6':
        print("Exiting the program.")
        break
    else:
        print("Invalid choice, please try again.")


