class BankAccont:
    def __init__(self, balence, account):
        self.__balance= balence
        self.__account= account
    def display_acc(self):
        print(self.__balance)
    def deposit(self,dep):
        self.__balance+=dep
        print(self.__balance)
    def withdrawal(self, withd):
        self.__balance-=withd
        print(self.__balance)
d1=BankAccont(10,100)
d1.deposit(10)
d1.withdrawal(10)
