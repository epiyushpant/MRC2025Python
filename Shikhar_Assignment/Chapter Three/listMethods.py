# Demonstrate list methods
colors = ['red']

colors.append('blue')       # Add to end
colors.insert(0, 'green')   # Insert at start
colors.extend(['yellow'])   # Add multiple
print("After additions:", colors)

colors.remove('blue')       # Remove by value
colors.pop(2)               # Remove by index
print("After removals:", colors)

print("Index of 'red':", colors.index('red'))
print("Count of 'red':", colors.count('red'))
colors.sort()
print("Sorted:", colors)