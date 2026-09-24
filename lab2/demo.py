# Demo script for the Account class.
# It creates a couple of sample accounts and prints them to show how the object behaves.
from account import Account

# create a fully-specified account and a blank default account
account1 = Account("Alice", 100)
account2 = Account()

# print both objects so the __str__ method formats them nicely
print(account1)
print(account2)