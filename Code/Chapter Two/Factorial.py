# Find the factorial of a number using both for and while loops.

# Write a program to find the factorial of a number using both for and while loops.

def factorial_for(n):
    if n < 0:
        return "Factorial is not defined for negative numbers."
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

def factorial_while(n):
    if n < 0:
        return "Factorial is not defined for negative numbers."
    result = 1
    i = 1
    while i <= n:
        result *= i
        i += 1
    return result

# Example usage
if __name__ == "__main__":
    try:
        number = int(input("Enter a non-negative integer to find its factorial: "))
        print(f"Factorial of {number} using for loop: {factorial_for(number)}")
        print(f"Factorial of {number} using while loop: {factorial_while(number)}")
    except ValueError:
        print("Please enter a valid non-negative integer.")
    