class BankAccount:
    def __init__(self, initial_balance = 0):
        self.balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
        else:
            raise ValueError("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
        else:
            raise ValueError("Invalid withdraw amount.")

    def check_balance(self):
        return self.balance
    
    def __str__(self):
        return f"This checking account has a balance of ${self.balance}."
    

class SavingsAccount:
    def __init__(self, initial_balance = 0, interest_rate = 0.02):
        self.balance = initial_balance
        self.interest_rate = interest_rate

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
        else:
            raise ValueError("Amount must be positive.")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
        else:
            raise ValueError("Invalid withdraw amount.")

    def check_balance(self):
        return self.balance
    
    def apply_interest(self):
        self.balance *= (1 + self.interest_rate)

    def __str__(self):
        return f"This savings account has a balance of ${self.balance} and an interest rate of {self.interest_rate*100}%"