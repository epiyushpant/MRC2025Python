
# Keep asking the user to input a valid age (between 1 to 100) using a loop.
# If the user enters an invalid age, prompt them to try again.

while True:
    try:
        age = int(input("Please enter your age (1-100): "))
        if 1 <= age <= 100:
            print(f"Thank you! Your age is {age}.")
            break
        else:
            print("Invalid age. Please enter a number between 1 and 100.")
    except ValueError:
        print("Invalid input. Please enter a number between 1 and 100.")