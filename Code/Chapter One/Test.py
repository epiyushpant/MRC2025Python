import random

secret_number = random.randint(1, 10)  # Random number between 1 and 10

while True:
    guess = int(input("Guess the number (1-10): "))

    if guess < 1 or guess > 10:
        print("Invalid number! Try again.")  # Skip invalid inputs
        continue  # Goes to the next iteration without checking further

    if guess == secret_number:
        print("Congratulations! You guessed it right.")
        break  # Stops the loop when the correct number is guessed

    print("Wrong guess, try again!")  # Continues the loop
