# Create 3 files in the classes directory car.py, fruit.py, and bank.py. Define the following classes in each module respectively.
# Car
# Fruit
# Account
# Each class should have one class attribute and three instance variables.
class Account:
    bank_name = "Equity Bank"
    def __init__(self, account_number, account_type, balance):
        self.account_number = account_number
        self.account_type = account_type
        self.balance = balance