
# Variables - They can change during program execution
age = 25  # integer variable
print(f"\nMy age is {age} (type: {type(age)})")

age = 26  # value can be changed
print(f"Now my age is {age}")

# Constants - By convention, we use uppercase names (but can still be changed)
PI = 3.14159  # treated as constant by naming convention
print(f"\nThe value of PI is approximately {PI} (type: {type(PI)})")

# Basic Data Types in Python
# Integer
students_count = 30
print(f"\nStudents: {students_count} (type: {type(students_count)})")

# Float
temperature = 98.6
print(f"Temperature: {temperature} (type: {type(temperature)})")

# String
greeting = "Hello, Python!"
print(f"Greeting: {greeting} (type: {type(greeting)})")

# Boolean
is_raining = False
print(f"Is it raining? {is_raining} (type: {type(is_raining)})")

# NoneType
result = None
print(f"Result: {result} (type: {type(result)})")

# Type Conversion (Type Casting)
# Implicit conversion (automatically done by Python)
num_int = 5
num_float = 2.5
result = num_int + num_float  # int is converted to float
print(f"\nImplicit conversion: {num_int} + {num_float} = {result} (type: {type(result)})")

# Explicit conversion (done manually by programmer)
print("\nExplicit conversions:")

# String to integer
user_input = "42"
try:
    number = int(user_input)
    print(f"String '{user_input}' converted to integer: {number} (type: {type(number)})")
except ValueError:
    print(f"Could not convert '{user_input}' to integer!")

# Integer to float
int_num = 7
float_num = float(int_num)
print(f"Integer {int_num} converted to float: {float_num} (type: {type(float_num)})")

# Float to integer (loses decimal part)
float_num = 9.99
int_num = int(float_num)
print(f"Float {float_num} converted to integer: {int_num} (type: {type(int_num)})")

# Number to string
price = 19.99
price_str = str(price)
print(f"Float {price} converted to string: '{price_str}' (type: {type(price_str)})")

# Boolean conversion
print("\nBoolean conversions:")
print(f"int(True) = {int(True)}")  # 1
print(f"int(False) = {int(False)}")  # 0
print(f"bool(1) = {bool(1)}")  # True
print(f"bool(0) = {bool(0)}")  # False
print(f"bool('Hello') = {bool('Hello')}")  # True
print(f"bool('') = {bool('')}")  # False

# Handling Invalid Conversions with try-except

invalid_input = "abc123"
try:
    number = int(invalid_input)
    print(f"\nConverted value: {number}")
except ValueError as e:
    print(f"\nError converting '{invalid_input}' to integer: {e}")

# Getting User Input and Converting Types

try:
    # Get user input (always comes as string)
    user_age = input("Please enter your age: ")
    
    # Convert to integer
    age = int(user_age)
    print(f"In 10 years, you'll be {age + 10} years old.")
    
    # Get height input
    user_height = input("Please enter your height in meters (e.g., 1.75): ")
    height = float(user_height)
    print(f"Your height is {height} meters.")
    
except ValueError:
    print("Please enter valid numbers for age and height!")