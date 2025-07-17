# 1. Built-in function
print(len("Hello World"))

# 2. User-defined function
def greet(name):
    return f"Hello, {name}!"

print(greet("Alice"))

# 3. Lambda function
square = lambda x: x * x
print(square(5))

# 4. Function with default argument
def power(base, exponent=2):
    return base ** exponent

print(power(3))
print(power(3, 3))

# 5. Function with variable-length arguments
def add_numbers(*args):
    return sum(args)

print(add_numbers(1, 2, 3, 4))