class Account:
    def __init__(self, owner="", balance=0.0):
        self.owner = owner
        self.balance = balance

    def __str__(self):
        return f"Owner: {self.owner}, Balance: ${self.balance:.2f}"