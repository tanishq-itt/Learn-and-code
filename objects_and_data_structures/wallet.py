class Wallet:
    def __init__(self, balance):
        self._balance = balance 

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, value):
        if value < 0:
            raise ValueError("Balance cannot be negative")
        self._balance = value

    def withdraw(self, amount):
        if amount <= self._balance:
            self._balance -= amount
            return True
        return False
