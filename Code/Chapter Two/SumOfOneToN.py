#Sum of all numbers from 1 to N entered by the user.

def sum_of_numbers(n):
    if n < 1:
        return "Please enter a positive integer."
    
    total = 0
    for i in range(1, n + 1):
        total += i
    
    return total

# Example usage
if __name__ == "__main__":  
    try:
        user_input = int(input("Enter a positive integer: "))
        result = sum_of_numbers(user_input)
        print(f"The sum of all numbers from 1 to {user_input} is: {result}")
    except ValueError:
        print("Please enter a valid positive integer.")



