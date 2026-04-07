def atm_program():
    """ATM simulation program using Python."""
    
    # Initialize account balance and correct PIN
    balance = 5000.0
    correct_pin = 1234

    print("Welcome to ATM Machine")
    
    try:
        # Ask user to enter PIN
        pin = int(input("Please enter your PIN: "))

        # Verify PIN
        if pin == correct_pin:
            print("Login Successful")

            # Menu loop for ATM operations
            while True:
                print("\n1. Check Balance")
                print("2. Deposit Amount")
                print("3. Withdraw Amount")
                print("4. Exit")
                
                # Take user choice
                option = int(input("Enter your choice: "))

                # Check balance
                if option == 1:
                    print(f"Your current balance is: {balance:.2f}")

                # Deposit money
                elif option == 2:
                    deposit = float(input("Enter amount to deposit: "))
                    if deposit > 0:
                        balance += deposit
                        print("Amount Deposited Successfully")
                        print(f"Updated Balance: {balance:.2f}")
                    else:
                        print("Enter valid deposit amount")

                # Withdraw money
                elif option == 3:
                    withdraw = float(input("Enter amount to withdraw: "))
                    if withdraw > 0 and withdraw <= balance:
                        balance -= withdraw
                        print("Amount Withdrawn Successfully")
                        print(f"Updated Balance: {balance:.2f}")
                    elif withdraw > balance:
                        print("Insufficient funds")
                    else:
                        print("Enter valid withdrawal amount")

                # Exit the program
                elif option == 4:
                    print("Thank you for using the ATM. Goodbye!")
                    break

                # Handle invalid menu choice
                else:
                    print("Invalid option. Please try again.")
        
        # Incorrect PIN case
        else:
            print("Incorrect PIN. Exiting.")

    # Handle invalid (non-numeric) input
    except ValueError:
        print("Invalid input. Please enter numbers only.")

# Run the program
if __name__ == "__main__":
    atm_program()
