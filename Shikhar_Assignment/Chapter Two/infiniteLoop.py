# Menu system that runs until user quits
while True:
    print("\n1. Say hello")
    print("2. Get current time")
    print("3. Quit\n")
    
    choice = input("Enter choice: ")
    
    if choice == '1':
        print("Hello!")
    elif choice == '2':
        from datetime import datetime
        print("Current time:", datetime.now().time())
    elif choice == '3':
        print("Goodbye!")
        break  # Exit loop
    else:
        print("Invalid choice!")