# Create a menu-driven program using infinite loop and break to allow user to choose options like add, subtract, exit etc.


def menu():
    while True:
        print("\nMenu:")
        print("1. Add")
        print("2. Subtract")
        print("3. Exit")
        choice = input("Enter your choice (1-3): ")

        if choice == "1":
            try:
                a = float(input("Enter first number: "))
                b = float(input("Enter second number: "))
                print(f"Result: {a} + {b} = {a + b}")
            except ValueError:
                print("Invalid input! Please enter numbers.")
        elif choice == "2":
            try:
                a = float(input("Enter first number: "))
                b = float(input("Enter second number: "))
                print(f"Result: {a} - {b} = {a - b}")
            except ValueError:
                print("Invalid input! Please enter numbers.")
        elif choice == "3":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice! Please select 1, 2, or 3.")

if __name__ == "__main__":
    menu()
