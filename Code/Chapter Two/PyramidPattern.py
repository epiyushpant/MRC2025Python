# Print a number pyramid pattern.

def print_number_pyramid(rows):
    for i in range(1, rows + 1):
        # Print leading spaces
        print(" " * (rows - i), end="")
        # Print numbers with spaces
        for j in range(1, i + 1):
            print(j, end=" ")
        print()  # Move to the next line after each row

# Example usage
if __name__ == "__main__":
    try:
        num_rows = int(input("Enter the number of rows for the pyramid: "))
        if num_rows < 1:
            print("Please enter a positive integer.")
        else:
            print_number_pyramid(num_rows)
    except ValueError:
        print("Invalid input! Please enter a valid integer.")