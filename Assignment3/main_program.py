from bankutils import BankAccount, SavingsAccount

def Bank_Account_Tests():
    print("\nBank account 1 Tests")
    account1 = BankAccount()
    try:
        account1.deposit(1000)
        account1.withdraw(2000)
    except ValueError as e:
        print("Error:", e)
    else:
        print("Bank account 1 transactions completed successfully.")
    finally:
        print("Finished account1 transaction block.")

    try:
        account1.withdraw(500)
    except ValueError as e:
        print("Error:", e)
    else:
        print("Withdrawal completed successfully.")
    finally:
        print("Finished second account1 transaction block.")

    print(account1.check_balance())
    print(account1)

    print("\nBank account 2 Tests")
    account2 = BankAccount(50)
    try:
        account2.deposit(-1)
    except ValueError as e:
        print("Error:", e)
    else:
        print("Deposit completed successfully.")
    finally:
        print("Finished account2 deposit block.")

    try:
        account2.withdraw(-1)
    except ValueError as e:
        print("Error:", e)
    else:
        print("Withdrawal completed successfully.")
    finally:
        print("Finished account2 withdrawal block.")

    print(account2.check_balance())
    print(account2)

def Savings_Account_Tests():
    print("\nSavings account 1 Tests")
    account1 = SavingsAccount()
    try:
        account1.deposit(100)
        account1.apply_interest()
    except ValueError as e:
        print("Error:", e)
    else:
        print("Savings account 1 operations completed successfully.")
    finally:
        print("Finished savings account1 block.")

    print(account1.check_balance())

    try:
        account1.withdraw(50)
    except ValueError as e:
        print("Error:", e)
    else:
        print("Withdrawal completed successfully.")
    finally:
        print("Finished savings account1 withdrawal block.")

    print(account1)

    print("\nSavings account 2 Tests")
    account2 = SavingsAccount(1000, .10)
    try:
        account2.apply_interest()
        account2.apply_interest()
        print(account2.check_balance())
        account2.deposit(-1)
    except ValueError as e:
        print("Error:", e)
    else:
        print("Savings account 2 deposit completed successfully.")
    finally:
        print("Finished savings account2 deposit block.")

    try:
        account2.withdraw(100000)
    except ValueError as e:
        print("Error:", e)
    else:
        print("Withdrawal completed successfully.")
    finally:
        print("Finished savings account2 withdrawal block.")

    print(account2)

if __name__ == "__main__":
    Bank_Account_Tests()
    Savings_Account_Tests()