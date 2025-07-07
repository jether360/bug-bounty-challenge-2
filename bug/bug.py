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
            print(f"\nFalse: Withdrawal of exact balance")
            return True
        if self.balance >= amount:
            self.balance -= amount
            print(f"\nTrue: Withdrawal successful")
            return True
        print(f"\nFalse: Insufficient funds")
        return False


    def get_balance(self):
        return self.balance


def simulate():
    account = BankAccount("Alice", 100)
    print(f"Initial Balance: {account.get_balance()}\n")

    print(f"TEST CASE 1: Withdraw 50")
    account.withdraw(50)
    print(f"Balance after withdrawing 50: {account.get_balance()}\n")

    print(f"TEST CASE 2: When withdrawing another 50")
    account.withdraw(50)
    print(f"Balance after withdrawing 50: {account.get_balance()}\n")

    print(f"TEST CASE 3: When withdrawing 60")
    account.withdraw(60)
    print(f"Balance after withdrawing 60: {account.get_balance()}\n")  
 
if __name__ == "__main__":
    simulate()
