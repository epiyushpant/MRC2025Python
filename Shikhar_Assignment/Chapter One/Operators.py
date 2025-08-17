# Arithmetic Operators
a = 15
b = 3

print("\nArithmetic Operators:")
print(f"Addition: {a} + {b} = {a + b}")
print(f"Subtraction: {a} - {b} = {a - b}")
print(f"Multiplication: {a} * {b} = {a * b}")
print(f"Division: {a} / {b} = {a / b}")
print(f"Floor Division: {a} // {b} = {a // b}")
print(f"Modulus: {a} % {b} = {a % b}")
print(f"Exponentiation: {a} ** {b} = {a ** b}")

# Comparison Operators
x = 10
y = 20

print("\nComparison Operators:")
print(f"x == y: {x == y}")
print(f"x != y: {x != y}")
print(f"x > y: {x > y}")
print(f"x < y: {x < y}")
print(f"x >= y: {x >= y}")
print(f"x <= y: {x <= y}")

# Logical Operators
p = True
q = False

print("\nLogical Operators:")
print(f"p and q: {p and q}")
print(f"p or q: {p or q}")
print(f"not p: {not p}")

# Assignment Operators
z = 5
z += 3  # z = z + 3
print("\nAssignment Operators:")
print(f"z += 3: {z}")

z *= 2  # z = z * 2, z is 8 now so, 8 * 2
print(f"z *= 2: {z}")

# Bitwise Operators
a = 10  # 1010 in binary
b = 4   # 0100 in binary

print("\nBitwise Operators:")
print(f"a & b: {a & b}")  # AND
print(f"a | b: {a | b}")  # OR
print(f"a ^ b: {a ^ b}")  # XOR
print(f"~a: {~a}")         # NOT
print(f"a << 1: {a << 1}")  # Left shift
print(f"a >> 1: {a >> 1}")  # Right shift

# Membership Operators
lst = [1, 2, 3, 4, 5]

print("\nMembership Operators:")
print(f"3 in lst: {3 in lst}")
print(f"6 not in lst: {6 not in lst}")

# Identity Operators
a = [1, 2, 3]
b = [1, 2, 3]
c = a

print("\nIdentity Operators:")
print(f"a is b: {a is b}")    # False, because a and b are different objects
print(f"a is c: {a is c}")    # True, because a and c refer to the same object