# Use continue to skip printing even numbers in a loop.

def print_odd_numbers(limit):
    for num in range(limit):
        if num % 2 == 0:
            continue  # Skip even numbers
        print(num)

# Example usage
if __name__ == "__main__":      
    limit = int(input("Enter a limit: "))
    print("Odd numbers up to", limit, ":")
    print_odd_numbers(limit)
    