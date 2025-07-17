# Different  Type of Exceptions in Python

try:
    # ZeroDivisionError
    result = 10 / 0
except ZeroDivisionError as zde:
    print(f"Caught ZeroDivisionError: {zde}")

try:
    # ValueError
    num = int("abc")
except ValueError as ve:
    print(f"Caught ValueError: {ve}")

try:
    # IndexError
    lst = [1, 2, 3]
    print(lst[5])
except IndexError as ie:
    print(f"Caught IndexError: {ie}")

try:
    # KeyError
    d = {"a": 1}
    print(d["b"])
except KeyError as ke:
    print(f"Caught KeyError: {ke}")

try:
    # Handling multiple exceptions together
    x = int("xyz")
    y = [1, 2]
    print(y[10])
except (ValueError, IndexError) as e:
    print(f"Caught ValueError or IndexError: {e}")

# Example to show multiple exceptions in a single try block 

try:
    # Attempting to open a non-existent file
    with open('non_existent_file.txt', 'r') as f:
        content = f.read()
except (FileNotFoundError, IOError) as e:
    print(f"Caught FileNotFoundError or IOError: {e}")



# Example of raising an exception
def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b
try:
    result = divide(10, 0)
except ValueError as ve:
    print(f"Caught ValueError: {ve}")



# First one errro then generic error 
try:
    # Attempting to convert a string to an integer
    num = int("abc")
except ValueError as ve:
    print(f"Caught ValueError: {ve}")
except Exception as e:
    print(f"Caught a generic exception: {e}")


# Example of handling a specific exception followed by a generic exception

try:
    with open("ghost.txt", "r") as f:
        content = f.read()

except FileNotFoundError as fnfe:
    print(f"Caught FileNotFoundError: {fnfe}")

except Exception as e:
    print(f"Caught generic exception: {e}")


# Example of raise exception with custom message
def check_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative")
    return age
try:    
    age = check_age(-5)
except ValueError as ve:    

    print(f"Caught ValueError: {ve}")
# Example of catching multiple exceptions with a single except block
try:
    

