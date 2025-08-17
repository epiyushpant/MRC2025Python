# Bank Account with __init__
class BankAccount:
    def __init__(self, account_holder, balance=0):
        self.holder = account_holder
        self.balance = balance
        print(f"Account created for {self.holder} with balance Rs.{self.balance}")

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited Rs.{amount}. New balance: Rs.{self.balance}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew Rs.{amount}. New balance: Rs.{self.balance}")
        else:
            print("Insufficient funds!")

# Create account
account1 = BankAccount("Shikhar", 1000)
account1.deposit(500)
account1.withdraw(200)