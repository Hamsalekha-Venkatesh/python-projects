class Account:
    def __init__(self, title=None, balance=0):
        self.title = title
        self.balance = balance

    def withdrawal(self, amount):
        if self.balance >= amount:
            self.balance -= amount

    def deposit(self, amount):
        self.balance += amount

    def get_balance(self):
        return self.balance


class SavingsAccount(Account):
    interest_rate = None

    def __init__(self, title=None, balance=0, interest_rate=0):
        super().__init__(title, balance)
        self.interest_rate = interest_rate
