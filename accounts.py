import datetime
import pytz

class Account:
    """Simple class with balance"""

    def __init__(self,name, balance):
        self.name = name
        self.balance = balance
        self.transaction_list = []
        print("Account created for " + self.name)

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.show_balance()
            self.transaction_list.append((pytz.utc.localize(datetime.datetime.utcnow()), amount))


    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
        else:
            print("The amount must be greater than zero and no more than your account balance")
        self.show_balance()

    def show_balance(self):
        print("Balance is {}".format(self.balance))

    def show_transactions(self):
        for date, amount in self.transaction_list:
            if amount > 0:
                trans_type = "dedposited"
            else:
                trans_tyepe = "withdrawn"
                amount = amount * 1
            print("{:6} {} on {} (local time was {})".format(amount, tran_type, date, date.astimezone()))



if __name__ == '__main__':
    tim = Account("Tim", 0)
    tim.show_balance()

    tim.deposit(1000)
    #tim.show_balance()
    tim.withdraw(500)
    #tim.show_balance()

    tim.withdraw(2000)
