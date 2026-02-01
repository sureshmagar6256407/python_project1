gemailStore = { 
    "suresh6256406@gmail.com": "Sureshpun2022"
}

while True:  
    print("----WELCOME TO GEMAIL----")
    print("1. Login")
    print("2. Create New account")
    print("3. Exit")

    choice = input("Enter your choice :: ")  
    if choice == "1":
        email = input("Enter your email :: ")  
        password = input("Enter your pw :: ")  
        if email in gemailStore and gemailStore[email] == password:
            print("✓ Login successful!")
        else:
            print("✗ Invalid email or password")

    elif choice == "2":
        email = input("Enter the email you want to create :: ")  
        password = input("Enter the new password :: ")  
        if email in gemailStore:
            print("✗ Email already exists")
        else:
            # Check if email contains @, ., and 'gmail'
            if '@' in email and '.' in email and 'gmail' in email:
                # Check for exactly one @ and valid format
                if email.count('@') == 1 and email.endswith('.com'):
                    # Additional check: format should be something@gmail.com
                    if email.endswith('@gmail.com'):
                        gemailStore[email] = password  
                        print("✓ Your email has been created successfully.")
                    else:
                        print("✗ Invalid email format. Use format: name@gmail.com")
                else:
                    print("✗ Invalid email format. Please ensure it has exactly one '@' and ends with '.com'.")
            else:
                print("✗ Invalid email format. Please ensure it is a valid Gmail address.")
    elif choice == "3":
        print("✓ Exiting the program. Goodbye!")
        break
    else:
        print("✗ Invalid choice. Please enter 1, 2, or 3.")