#Programmer: Amna(23k-0066)
#Date: 18th Sept 2024

class Account:
    def __init__(self, account_no ,account_bal ,security_code):
        self.__account_no = account_no
        self.__account_bal = account_bal
        self.__security_code = security_code

    def print(self):
        print("Account no: ", self.__account_no)
        print("Balance: ", self.__account_bal)
        print("Security code: ", self.__security_code)



account1 = Account(23000987, 245.670, 3426)
account1.print()