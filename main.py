from bank_account import BankAccount

def main():
    account = BankAccount("Mansour", 999)

    account.deposit(1)
    print(f" your account has: {account.get_balance()}")


    try:
        account.withdraw(1001)
        print(f" your account has: {account.get_balance()}")
    except Exception as e:
        print(f"withrdaw denied {e}")

    
    print(f"this account belongs to {account.get_account_holder()}")
    print(f"you current balance is {account.get_balance()}")

    
main()

    