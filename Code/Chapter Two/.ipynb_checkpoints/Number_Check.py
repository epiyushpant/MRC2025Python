#Write a program to check if a number is positive, negative or zero using if.

def check_number(num):
    if num > 0:
        return "The number is positive."
    elif num < 0:
        return "The number is negative."
    else:
        return "The number is zero."
    
# Example usage
# Example usage
try:
    user_input = float(input("Enter a number: "))
    result = check_number(user_input)
    print(result)
except ValueError:
    print("Please enter a valid number.")

