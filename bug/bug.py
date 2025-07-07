class BankAccount:
    def __init__(self, account_holder: str, balance: float):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount: float):
        if amount > 0:
            self.balance += amount

    def withdraw(self, amount: float):
        if amount < 0:
            raise ValueError("Cannot withdraw negative amount.")
        if self.balance >= amount:
            self.balance -= amount
            return True
        return False

    def get_balance(self):
        return self.balance


def simulate():
    account = BankAccount("Alice", 100)
    print(f"Initial Balance: {account.get_balance()}")

    account.withdraw(50)
    print(f"Balance after withdrawing 50: {account.get_balance()}")

    account.withdraw(60)
    print(f"Balance after withdrawing 60: {account.get_balance()}")  


if __name__ == "__main__":
    simulate()
