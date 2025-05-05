import datetime
import uuid
import time


class Transcation:
    def init(system, transcation_type, amount, timestamp=None):
        system.transcation_id = str(uuid.uuid4())
        system.transcation_type = transcation_type
        system.amount = amount
        system.timestamp = timestamp if timestamp else datetime.datetime.now().strftime(
            "%Y-%m-%d %H:%M:%S")


class Account:
    def init(system, account_id, owner_name, balance=0, username=None, password=None):
        system.account_id = account_id
        system.owner_name = owner_name
        system.balance = balance
        system.transaction_history = []
        system.creation_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        system.last_access = self.creation_date
        system.username = username
        system.password = password


def deposit(balance, amount):
    customer = user_verification()
    if amount <= 0:
        print("Invalid deposit amount.Must be greater than 0. ")

        return balance
    balance += amount
    print(f"Successfully deposited Rs.{amount}.New balance:Rs.{balance}")
    return balance


def withdraw(balance, amount):
    customer = user_verification()
    if amount <= 0:
        print("Invalid withdrawal amount.Must be greater than 0.")
    elif amount > balance:
        print("Insufficient funds.")
    else:
        balance -= amount
        print(f"Successfully withdrawn Rs.{amount}.New balance:Rs{balance}")
    return balance


def main():
    bank = bank

    while True:
        print("\n===Bank Menu===")
        print("1.Create a New Account")
        print("2.Make a Deposit")
        print("3.Make a Withdraw")
        print("4.View Transcation History")
        print("5.Check Balance")
        print("6.Transfer Money")
        print("7.List all Accounts")
        print("8.Exit")

        choice = input("Choose an option(1-6):")

        if choice == '1':
            account_number = input("Enter account number: ")
            name = input("Enter account holder name: ")
            initial_deposit = float(
                input("Enter initial deposit (default 0): "))
            bank.create_account(account_number, name, initial_deposit)

        if choice == '2':
            try:
                amount = float(input("Enter deposit amount:Rs."))
                balance = deposit(balance, amount)
            except ValueError:
                print("Please enter a valid number.")

        elif choice == '3':
            try:
                amount = float(input("Enter withdrawal amount:Rs"))
                balance = withdraw(balance, amount)
            except ValueError:
                print("Please enter a valid number.")

        elif choice == '4':
            print(f"Current balance:Rs{balance}")

        elif choice == '4':
            print("Thanks you for using our service. Goodbye!")
            break

        else:
            print("Invalid option. Please select 1,2,3 or 4.")


main()
