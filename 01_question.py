'''
1. Create a class BankAccount with attributes account_holder, balance, and methods deposit() and withdraw(). Implement logic to prevent withdrawing more than the available balance.
'''

class BankAccount:
    def __init__(self, account_holder, balance = 0):
        self.account_holder = account_holder
        self.balance = balance
    
    def deposit(self, amount):
        self.balance += amount
        return f"Deposited {amount}. New Balance:{self.balance}"
    
    def Withdraw(self, amount):
        if amount > self.balance:
            return "Insufficient balance"
        self.balance -= amount
        return f"Withdraw:{amount}, New Balance: {self.balance}"    

account = BankAccount("Mohan", 10000)
print(account.deposit(100))
print(account.Withdraw(100))