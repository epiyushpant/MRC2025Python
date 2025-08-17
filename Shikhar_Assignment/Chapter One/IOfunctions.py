# # Reading input from the user (input function)
name = input("Enter your name: ")  # Prompt user to input their name
age = int(input("Enter your age: "))  # Prompt user to input their age, converting it to integer

# Displaying output using the print function
print(f"Hello, {name}! You are {age} years old.")

# Writing to a file with comprehensive exception handling
try:
    # Define variables to write to file
    name = "Shikhar Basnet"
    age = 23
    
    # Attempt to open and write to the file
    with open('output.txt', 'w') as file:
        file.write(f"Name: {name}\n")
        file.write(f"Age: {age}\n")
    
    print(f"File written successfully! Name: {name}, Age: {age}")
    
except Exception as e:
    print(f"An unexpected error occurred: {e}")

# Reading from a file using read() function
with open('output.txt', 'r') as file:
    content = file.read()
    print("\nReading Content of output.txt:")
    print(content)