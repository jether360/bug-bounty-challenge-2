class BankAccount:
    def __init__(self, account_holder: str, balance: float):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount: float):
        if amount > 0:
            self.balance += amount

    def withdraw(self, amount: float):
        if amount < 0:
            raise ValueError(f"Cannot withdraw negative amount.")
        if self.balance == amount: 
            print(f"\nFalse withdrawal of exact balance")
            return True
        if self.balance >= amount:
            self.balance -= amount
            print(f"\nTrue: Withdrawal of {amount} successful")
            return True
        print(f"\nFalse: Insufficient funds")
        return False


    def get_balance(self):
        return self.balance


def simulate():
    account = BankAccount("Alice", 100)
    print(f"Initial Balance: {account.get_balance()}\n")

    account.withdraw(50)
    print(f"Balance after withdrawing 50: {account.get_balance()}")

    account.withdraw(50)
    print(f"Balance after withdrawing 50: {account.get_balance()}")  
 

if __name__ == "__main__":
    simulate()
