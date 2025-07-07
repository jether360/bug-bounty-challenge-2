class BankAccount:
    def __init__(self, account_holder: str, balance: float):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount: float):
        if amount > 0:
            self.balance += amount
        #Added
        if amount < 1:
            print("Error: Invalid Input")
    def withdraw(self, amount: float):
        if amount < 0:
            print("Error: Cannot withdraw negative amount.")
            print(f"Balance: {self.balance}")
            return False
        if self.balance >= amount:
            self.balance -= amount
            #Added
            print(f"Balance after withdrawing {amount}: {self.balance}")
            return True
        #Added
        if amount > self.balance:
            print(f"Withdrawal of {amount} failed: : insufficient funds.")
            print(f"Balance after withdrawing {amount}: {self.balance} ❌")
            return False
        return False

    def get_balance(self):
        return self.balance


def simulate():
    
    account = BankAccount("Alice", 100)
    print(f"Initial Balance: {account.get_balance()}")

    
    account.withdraw(50)
    account.withdraw(60)
    
if __name__ == "__main__":
    simulate()
