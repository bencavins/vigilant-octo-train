# Linters: flake8, pylint


class Wallet:
    def __init__(self, init_balance=0):  # constructor
        self.balance = init_balance
        self.color = 'black'

    def add(self, amount):
        self.balance += amount

    def spend(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            raise RuntimeError("Insufficient funds")


class SmallWallet(Wallet):
    cap = 100

    def __init__(self, init_balance=0):  # constructor
        if init_balance <= self.cap:
            super().__init__(init_balance)
        else:
            raise RuntimeError(f"Wallet can't fit {init_balance}")
    
    def add(self, amount):
        if self.balance + amount > self.cap:
            raise RuntimeError('Wallet is full')
        else:
            self.balance += amount
    
    def describe(self):
        print(f"This wallet has ${self.balance} and is {self.color}")


if __name__ == '__main__':
    wallet = Wallet(25)
    print(wallet)