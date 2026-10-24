# Question 5: Banking Transaction System
# Concepts: Classes, inheritance, overriding, super()
# Scenario: A bank offers savings and current accounts. A savings account allows
# withdrawals only if sufficient balance remains. A current account allows
# withdrawals up to an overdraft limit.
# Task: Implement a parent class BankAccount and override withdraw() in
# CurrentAccount. Use super() to perform the regular withdrawal when sufficient
# funds are available.
# Sample input:
# Initial Balance: 5000
# Withdrawal: 3000
# Expected output:
# Withdrawal Successful
# Remaining Balance: 2000

class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            return True
        else:
            return False

class CurrentAccount(BankAccount):
    def __init__(self, balance, overdraft_limit):
        super().__init__(balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        if amount <= self.balance + self.overdraft_limit:
            super().withdraw(amount)
            return True
        else:
            return False

initial_balance = float(input("Initial Balance: "))
withdrawal_amount = float(input("Withdrawal: "))

account_type = input("Account Type(Savings/Current): ")
if account_type.lower() == "savings":
    account = BankAccount(initial_balance)
elif account_type.lower() == "current":
    overdraft_limit = float(input("Overdraft Limit: "))
    account = CurrentAccount(initial_balance, overdraft_limit)
else:
    print("Invalid account type")
    exit()  