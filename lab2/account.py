# A simple bank-account class used in the lab to practice object-oriented design.
# Each account stores an owner name and a balance, and can display itself neatly.
class Account:
    def __init__(self, owner="", balance=0.0):
        """Initialize the account with an owner and starting balance."""
        # store the account holder's name and the current balance value
        self.owner = owner
        self.balance = balance

    def __str__(self):
        """Return a readable summary showing the owner and balance."""
        # format the balance with two decimal places so it prints like money
        return f"Owner: {self.owner}, Balance: ${self.balance:.2f}"