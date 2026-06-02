def add(a, b, c=0):
    return a + b + c

print(add(2, 3))        # 5
print(add(2, 3, 4))     # 9



def add(*numbers):
    return sum(numbers)

print(add(2, 3))           # 5
print(add(1, 2, 3, 4))     # 10



def show_info(*args):
    if len(args) == 1:
        print("Name:", args[0])
    elif len(args) == 2:
        print("Name:", args[0], "| Age:", args[1])
    else:
        print("Too many arguments")

show_info("Alice")           # Name: Alice
show_info("Bob", 25)         # Name: Bob | Age: 25


