# Write a program to print a right-angled triangle using nested for loops.

def print_triangle(rows):
    for i in range(1, rows + 1):
        for j in range(i):
            print("*", end="")
        print()  # Move to the next line after each row

# Example usage
if __name__ == "__main__":
    try:
        num_rows = int(input("Enter the number of rows for the triangle: "))
        if num_rows < 1:
            print("Please enter a positive integer.")
        else:
            print_triangle(num_rows)
    except ValueError:
        print("Invalid input! Please enter a valid integer.")










