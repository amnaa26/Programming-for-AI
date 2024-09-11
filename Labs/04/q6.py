'''
Programmer: Amna(23k-0066)
Date: 11/Sept/2024
Q6) Write a Python class BankAccount with attributes like account_number, balance,
    date_of_opening and customer_name, and methods like deposit, withdraw, and
    check_balance.
'''

class BankAccount:
    def __init__(self, account_number, balance, date_of_opening, customer_name):
        self.account_number = account_number
        self.balance = balance
        self.date_of_opening = date_of_opening
        self.customer_name = customer_name

    def deposit(self, amount):
        """Deposit money into the account."""
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount}. New balance is ${self.balance}.")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        """Withdraw money from the account."""
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                print(f"Withdrew ${amount}. New balance is ${self.balance}.")
            else:
                print("Insufficient funds.")
        else:
            print("Withdrawal amount must be positive.")

    def check_balance(self):
        """Check the current balance of the account."""
        print(f"Current balance: ${self.balance}")

# Example usage
if __name__ == "__main__":
    account = BankAccount("123456789", 1000, "2024-09-10", "John Doe")
    account.check_balance()
    account.deposit(500)
    account.withdraw(200)
    account.check_balance()
