'''
Programmer: Amna(23k-0066)
Date: 11/Sept/2024
Q8) Write a program in which a class named Account has private member variables named
    account_no ,account_bal ,security_code. Use a public function to initialize the variables
    and print all data.
'''

class Account:
    def __init__(self):
        """Constructor to initialize the Account object."""
        self.__account_no = None
        self.__account_bal = None
        self.__security_code = None
    def initialize_and_print(self, account_no, account_bal, security_code):
        """Initialize private member variables and print all data."""
        self.__account_no = account_no
        self.__account_bal = account_bal
        self.__security_code = security_code
        self.__print_data()
    def __print_data(self):
        """Private method to print all account data."""
        print(f"Account Number: {self.__account_no}")
        print(f"Account Balance: ${self.__account_bal:.2f}")
        print(f"Security Code: {self.__security_code}")

# Example usage
if __name__ == "__main__":
    account = Account()
    account.initialize_and_print("123456789", 1500.75, "ABCD1234")
