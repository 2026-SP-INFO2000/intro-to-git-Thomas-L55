from bankutils import BankAccount, SavingsAccount

def Bank_Account_Tests():
    print("\nBank account 1 Tests")
    account1 = BankAccount()
    account1.deposit(1000)
    account1.withdraw(2000)
    account1.withdraw(500)
    print(account1.check_balance())
    print(account1)

    print("\nBank account 2 Tests")
    account2 = BankAccount(50)
    account2.deposit(-1)
    account2.withdraw(-1)
    print(account2.check_balance())
    print(account2)

def Savings_Account_Tests():
    print("\nSavings account 1 Tests")
    account1 = SavingsAccount()
    account1.deposit(100)
    account1.apply_interest()
    print(account1.check_balance())
    account1.withdraw(50)
    print(account1)

    print("\nSavings account 2 Tests")
    account2 = SavingsAccount(1000, .10)
    account2.apply_interest()
    account2.apply_interest()
    print(account2.check_balance())
    account2.deposit(-1)
    account2.withdraw(100000)
    print(account2)

if __name__ == "__main__":
    Bank_Account_Tests()
    Savings_Account_Tests()