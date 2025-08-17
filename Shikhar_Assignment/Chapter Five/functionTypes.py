# Function without arguments
def greet():
    print("Hello! Welcome to the program.")

# Function with arguments
def calculate_area(length, width):
    return length * width

# Value-returning function
def get_circle_area(radius):
    return 3.14 * radius ** 2

# Demonstration
greet()
rectangle_area = calculate_area(5, 3)
print(f"Rectangle area: {rectangle_area}")
print(f"Circle area: {get_circle_area(4)}")