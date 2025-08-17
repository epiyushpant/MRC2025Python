# Tuple operations (tuples are immutable)
my_tuple = (1, 2, 3)
print("Original Tuple:", my_tuple)

# "Adding" elements (creates new tuple)
new_tuple = my_tuple + (4,)
print("After 'Adding':", new_tuple)

# Cannot remove directly - convert to list
temp_list = list(new_tuple)
temp_list.remove(2)
modified_tuple = tuple(temp_list)
print("After 'Removing':", modified_tuple)

# Display
print("All Items:", temp_list)
