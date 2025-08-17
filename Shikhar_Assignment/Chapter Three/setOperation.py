# Set operations
fruits = {'apple', 'banana'}
print("Original Set:", fruits)

# Add elements
fruits.add('orange')
fruits.update(['kiwi', 'apple'])  # Duplicate ignored
print("After Adding:", fruits)

# Remove elements
fruits.remove('banana')
fruits.discard('mango')  # No error if missing
print("After Removing:", fruits)

# Display
print("Set Items:")
for item in fruits:
    print("-", item)