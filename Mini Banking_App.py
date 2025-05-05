import random
import datetime
import time

# Global dictionary to store all accounts
accounts = {}

def generate_account_number():
    """Generate a unique 8-digit account number"""
    while True:
        account_number = str(random.randint(10000000, 99999999))
        if account_number not in accounts:
            return account_number

def create_account():
    """Create a new bank account"""
    print("\n===== CREATE ACCOUNT =====")
    name = input("Enter account holder name: ")
    
    # Validate name
    if not name.strip():
        print("Error: Account holder name cannot be empty.")
        return
    
    # Get and validate initial balance
    try:
        initial_balance = float(input("Enter initial balance: $"))
        if initial_balance < 0:
            print("Error: Initial balance cannot be negative.")
            return
    except ValueError:
        print("Error: Please enter a valid amount.")
        return
    
    # Generate a unique account number
    account_number = generate_account_number()
    
    # Create the account
    accounts[account_number] = {
        'holder_name': name,
        'balance': initial_balance,
        'transactions': []
    }
    
    # Record initial deposit if balance > 0
    if initial_balance > 0:
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        accounts[account_number]['transactions'].append({
            'type': 'deposit',
            'amount': initial_balance,
            'timestamp': timestamp
        })
    
    print(f"Account created successfully!")
    print(f"Account Number: {account_number}")
    print(f"Holder Name: {name}")
    print(f"Initial Balance: ${initial_balance:.2f}")

def deposit_money():
    """Deposit money into an existing account"""
    print("\n===== DEPOSIT MONEY =====")
    account_number = input("Enter account number: ")
    
    # Check if account exists
    if account_number not in accounts:
        print("Error: Account does not exist.")
        return
    
    # Get and validate deposit amount
    try:
        amount = float(input("Enter deposit amount: $"))
        if amount <= 0:
            print("Error: Deposit amount must be positive.")
            return
    except ValueError:
        print("Error: Please enter a valid amount.")
        return
    
    # Update balance
    accounts[account_number]['balance'] += amount
    
    # Record transaction
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    accounts[account_number]['transactions'].append({
        'type': 'deposit',
        'amount': amount,
        'timestamp': timestamp
    })
    
    print(f"Deposit successful!")
    print(f"New Balance: ${accounts[account_number]['balance']:.2f}")

def withdraw_money():
    """Withdraw money from an existing account"""
    print("\n===== WITHDRAW MONEY =====")
    account_number = input("Enter account number: ")
    
    # Check if account exists
    if account_number not in accounts:
        print("Error: Account does not exist.")
        return
    
    # Get and validate withdrawal amount
    try:
        amount = float(input("Enter withdrawal amount: $"))
        if amount <= 0:
            print("Error: Withdrawal amount must be positive.")
            return
    except ValueError:
        print("Error: Please enter a valid amount.")
        return
    
    # Check if sufficient balance
    if amount > accounts[account_number]['balance']:
        print("Error: Insufficient balance.")
        return
    
    # Update balance
    accounts[account_number]['balance'] -= amount
    
    # Record transaction
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    accounts[account_number]['transactions'].append({
        'type': 'withdrawal',
        'amount': amount,
        'timestamp': timestamp
    })
    
    print(f"Withdrawal successful!")
    print(f"New Balance: ${accounts[account_number]['balance']:.2f}")

def check_balance():
    """Check the current balance of an account"""
    print("\n===== CHECK BALANCE =====")
    account_number = input("Enter account number: ")
    
    # Check if account exists
    if account_number not in accounts:
        print("Error: Account does not exist.")
        return
    
    print(f"Account Holder: {accounts[account_number]['holder_name']}")
    print(f"Current Balance: ${accounts[account_number]['balance']:.2f}")

def view_transaction_history():
    """View all transactions for an account"""
    print("\n===== TRANSACTION HISTORY =====")
    account_number = input("Enter account number: ")
    
    # Check if account exists
    if account_number not in accounts:
        print("Error: Account does not exist.")
        return
    
    print(f"Account Holder: {accounts[account_number]['holder_name']}")
    print(f"Current Balance: ${accounts[account_number]['balance']:.2f}")
    print("\nTransaction History:")
    
    if not accounts[account_number]['transactions']:
        print("No transactions found.")
        return
    
    print("Type       | Amount    | Date and Time")
    print("-" * 50)
    
    for transaction in accounts[account_number]['transactions']:
        transaction_type = transaction['type'].capitalize()
        amount = transaction['amount']
        timestamp = transaction['timestamp']
        print(f"{transaction_type:<10} | ${amount:<8.2f} | {timestamp}")

def transfer_money():
    """Transfer money between two accounts"""
    print("\n===== TRANSFER MONEY =====")
    from_account = input("Enter source account number: ")
    
    # Check if source account exists
    if from_account not in accounts:
        print("Error: Source account does not exist.")
        return
    
    to_account = input("Enter destination account number: ")
    
    # Check if destination account exists
    if to_account not in accounts:
        print("Error: Destination account does not exist.")
        return
    
    # Ensure accounts are different
    if from_account == to_account:
        print("Error: Cannot transfer to the same account.")
        return
    
    # Get and validate transfer amount
    try:
        amount = float(input("Enter transfer amount: $"))
        if amount <= 0:
            print("Error: Transfer amount must be positive.")
            return
    except ValueError:
        print("Error: Please enter a valid amount.")
        return
    
    # Check if sufficient balance
    if amount > accounts[from_account]['balance']:
        print("Error: Insufficient balance in source account.")
        return
    
    # Update balances
    accounts[from_account]['balance'] -= amount
    accounts[to_account]['balance'] += amount
    
    # Record transactions
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # Record in source account
    accounts[from_account]['transactions'].append({
        'type': 'transfer out',
        'amount': amount,
        'timestamp': timestamp,
        'to_account': to_account
    })
    
    # Record in destination account
    accounts[to_account]['transactions'].append({
        'type': 'transfer in',
        'amount': amount,
        'timestamp': timestamp,
        'from_account': from_account
    })
    
    print(f"Transfer successful!")
    print(f"New Balance in Source Account: ${accounts[from_account]['balance']:.2f}")
    print(f"New Balance in Destination Account: ${accounts[to_account]['balance']:.2f}")

def display_menu():
    """Display the main menu options"""
    print("\n===== MINI BANKING APPLICATION =====")
    print("1. Create Account")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Check Balance")
    print("5. Transaction History")
    print("6. Transfer Money")
    print("7. Exit")
    
    try:
        choice = int(input("Enter your choice (1-7): "))
        return choice
    except ValueError:
        print("Error: Please enter a number between 1 and 7.")
        return 0

def main():
    """Main function to run the banking application"""
    print("Welcome to the Mini Banking Application!")
    
    while True:
        choice = display_menu()
        
        if choice == 1:
            create_account()
        elif choice == 2:
            deposit_money()
        elif choice == 3:
            withdraw_money()
        elif choice == 4:
            check_balance()
        elif choice == 5:
            view_transaction_history()
        elif choice == 6:
            transfer_money()
        elif choice == 7:
            print("\nThank you for using the Mini Banking Application!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 7.")
        
        # Add a small delay for better readability
        time.sleep(1)

# Run the application
if __name__ == "__main__":
    main()