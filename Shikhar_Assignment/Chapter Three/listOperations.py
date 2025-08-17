# Create, modify, and display a list
my_list = [1, 2, 3]
print("Original List:", my_list)

# Add elements
my_list.append(4)
my_list.insert(1, 1.5)
print("After Adding:", my_list)

# Remove elements
my_list.remove(1.5)
popped = my_list.pop()
print("After Removing:", my_list, "| Popped:", popped)

# Display items
print("List Items:", my_list)