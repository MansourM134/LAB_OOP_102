
class BankAccount:
    def __init__(self, account_holder:str, initial_balance:float = 0):
       
        self.__account_holder = account_holder
        self.__initial_balance = initial_balance

    def deposit(self, amount:float):

        self.__initial_balance += amount
        return self.__initial_balance
    
    def withdraw(self, amount:float):


        if amount < 0:
            raise ValueError("amount cant be negative")
        if amount > self.__initial_balance:
            raise Exception("you dont have the funds")

        self.__initial_balance -= amount
        return self.__initial_balance
    
    def get_balance(self):
        return self.__initial_balance
    def get_account_holder(self):
        return self.__account_holder 



    