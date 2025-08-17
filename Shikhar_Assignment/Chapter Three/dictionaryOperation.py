# Dictionary operations
student = {'name': 'Alice', 'age': 20}
print("Original:", student)

# Add/Update
student['grade'] = 'A'
student['age'] = 21
print("After Changes:", student)

# Remove
del student['age']
popped = student.pop('grade')
print("After Removals:", student, "| Popped:", popped)

# Display
print("Key-Value Pairs:")
for key, value in student.items():
    print(f"{key}: {value}")