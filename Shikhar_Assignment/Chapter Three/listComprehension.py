# List comprehension examples
squares = [x**2 for x in range(1, 6)]
print("Squares:", squares)

even_numbers = [x for x in range(10) if x % 2 == 0]
print("Evens:", even_numbers)

words = ['Hi', 'Shikhar']
lengths = [len(word) for word in words]
print("Word lengths:", lengths)