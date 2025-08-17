while True:
    user_input = input("\nEnter a command (start/stop/pause/quit): ").lower()
    
    # Using if for special cases
    if user_input == "pause":
        print("System paused")
        continue
    if user_input == "quit":
        print("Goodbye!")
        break
    
    # Using match for the remaining cases
    match user_input:
        case "start":
            print("System starting...")
        case "stop":
            print("System stopping...")
        case _:
            print("Invalid command. Try again.")
    
    print("Command processed!")