# Programmer: Amna(23k-0066)
# Date: 28/Aug/2024
# Q8) Design a console based application for Converting different currency. You are required to ask user to choose input which currency you want to convert and then ask the amount. After that ask in which currency you want to convert. Then convert that currency into desired one...
#    (Currency should include Euro , Dollar, PkR, INR , and yen)


rates = {'USD': 1.0, 'EUR': 0.90, 'PKR': 278.89, 'INR': 83.89, 'YEN': 146.21}

print("Available currencies: EUR, USD, PKR, INR, YEN")
currency = input("Enter the currency you want to convert from: ")
amount = float(input("Enter amount: "))
original_amount = amount
changed_currency = input("Enter the currency you want to convert into: ")

if currency not in ['USD', 'EUR', 'PKR', 'INR', 'YEN'] or changed_currency not in ['USD', 'EUR', 'PKR', 'INR', 'YEN']:
        print("Invalid currency code. Please try again.")
        exit()

#Converting the amount into USD first
if currency != 'USD':
        amount = amount / rates[currency]

#Converting from USD to the target currency
if changed_currency != 'USD':
    amount = amount * rates[changed_currency]

print(f"{original_amount:.2f} {currency} is equal to {amount:.2f} {changed_currency}")
