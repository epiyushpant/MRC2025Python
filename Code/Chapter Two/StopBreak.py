# Use break to stop input when the user enters a specific keyword. (stop ) 

def check_number(num):
    if num > 0:
        return "The number is positive."
    elif num < 0:
        return "The number is negative."
    else:
        return "The number is zero."
# Example usage
while True:
    user_input = input("Enter a number (or type 'stop' to exit): ")
    if user_input.lower() == 'stop':
        print("Exiting the program.")
        break
    try:
        num = float(user_input)
        result = check_number(num)
        print(result)
    except ValueError:
        print("Please enter a valid number.")