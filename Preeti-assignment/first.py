# Python Program to Illustrate Variables, Constants, Data Types, and Type Conversion

# 1. VARIABLES
name = "Alice"        # String variable
age = 25              # Integer variable
height = 5.6          # Float variable
is_student = True     # Boolean variable

print("Variables:")
print("Name:", name)
print("Age:", age)
print("Height:", height)
print("Is Student:", is_student)
print()  # Blank line

# 2. CONSTANTS
PI = 3.14159
GRAVITY = 9.8

print("Constants:")
print("PI:", PI)
print("Gravity:", GRAVITY)
print()

# 3. DATA TYPES
print("Data Types:")
print("Type of name:", type(name))
print("Type of age:", type(age))
print("Type of height:", type(height))
print("Type of is_student:", type(is_student))
print()

# 4. TYPE CONVERSION
# Converting one data type to another

# Implicit Conversion (automatically by Python)
result = age + height  # int + float = float
print("Implicit Type Conversion:")
print("Result (age + height):", result)
print("Type of result:", type(result))
print()

# Explicit Conversion (manual conversion using functions)
age_str = str(age)             # int to string
height_int = int(height)       # float to int
is_student_int = int(is_student)  # bool to int (True = 1, False = 0)

print("Explicit Type Conversion:")
print("Age as string:", age_str, "->", type(age_str))
print("Height as int:", height_int, "->", type(height_int))
print("Is Student as int:", is_student_int, "->", type(is_student_int))
