#Print the first 10 Fibonacci numbers.

def fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    
    fib_sequence = [0, 1]
    for i in range(2, n):
        next_fib = fib_sequence[i - 1] + fib_sequence[i - 2]
        fib_sequence.append(next_fib)
    
    return fib_sequence

# Example usage
if __name__ == "__main__":
    try:
        count = int(input("Enter the number of Fibonacci numbers to generate: "))
        if count < 0:
            print("Please enter a non-negative integer.")
        else:
            fib_numbers = fibonacci(count)
            print(f"The first {count} Fibonacci numbers are: {fib_numbers}")
    except ValueError:
        print("Invalid input! Please enter a valid integer.")
