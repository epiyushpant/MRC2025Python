def password_system():
    correct_password = "secure123"
    max_attempts = 3
    timeout = 5  # seconds
    
    # 1. FOR LOOP - Limited attempts
    for attempt in range(1, max_attempts + 1):
        password = input(f"Attempt {attempt}/{max_attempts}: Enter password: ")
        
        # 2. CONTINUE - Skip empty inputs
        if not password:
            print("Password cannot be empty!")
            continue
            
        if password == correct_password:
            print("Access granted!")
            return True
        
        print("Incorrect password!")
    
    # 3. WHILE LOOP - Timeout after max attempts
    print(f"\nPlease wait for {timeout} seconds!")
    import time
    timeout_end = time.time() + timeout
    
    while time.time() < timeout_end:
        remaining = int(timeout_end - time.time())
        print(f"Please wait {remaining} seconds before trying again", end='\r')
        time.sleep(1)
    
    # 4. WHILE TRUE + BREAK - Final chance
    while True:
        password = input("\nLast chance: Enter password (type 'quit' to exit): ")
        
        if password.lower() == 'quit':
            break
            
        if password == correct_password:
            print("Access granted!")
            return True
            
        print("System locked. Contact administrator.")
        break

    return False

if __name__ == "__main__":
    if password_system():
        print("\nWelcome to the secure system!")
    else:
        print("\nAccess denied.")