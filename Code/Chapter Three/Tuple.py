# Write program to create tuple, add elements in tuple, remove elements from tuple and display tuple items.

# Start with an empty tuple
my_tuple = ()

# Convert tuple to list for easy modification
my_list = list(my_tuple)

# Add elements
my_list.append("apple")
my_list.append("banana")
my_list.append("cherry")

# Convert back to tuple and display
my_tuple = tuple(my_list)
print("Tuple items:", my_tuple)

# Remove an element
item_to_remove = "banana"
if item_to_remove in my_list:
    my_list.remove(item_to_remove)
else:
    print(f"Item '{item_to_remove}' not found in the tuple.")

# Convert back to tuple and display
my_tuple = tuple(my_list)
print("Tuple after removing", item_to_remove + ":", my_tuple)