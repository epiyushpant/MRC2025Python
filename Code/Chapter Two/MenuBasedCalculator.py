# Use match to create a simple menu-based calculator.

def add(x, y):
    return x + y
def subtract(x, y):
    return x - y
def multiply(x, y):
    return x * y
def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x / y

def calculator():
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    
    choice = input("Enter choice (1/2/3/4): ")
    
    if choice in ('1', '2', '3', '4'):
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            return "Invalid input! Please enter numeric values."
        
        match choice:
            case '1':
                return f"Result: {add(num1, num2)}"
            case '2':
                return f"Result: {subtract(num1, num2)}"
            case '3':
                return f"Result: {multiply(num1, num2)}"
            case '4':
                return f"Result: {divide(num1, num2)}"
    else:
        return "Invalid choice! Please select a valid operation."
    

# Example usage
if __name__ == "__main__":
    result = calculator()
    print(result)
# This code implements a simple menu-based calculator using match-case statements.
# It allows the user to select an operation and perform calculations with two numbers.
# The calculator supports addition, subtraction, multiplication, and division.
