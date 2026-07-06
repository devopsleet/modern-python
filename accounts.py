# import cat
import datetime, pytz
class Account:
    """Simple account class"""

    def __init__(self, name, balance):
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
            print("The amount should be greater than zero and no more than your account balance")
        self.show_balance()

    def show_balance(self):
        print(f"Balance is {self.balance}")

    def show_transactions


if __name__ == '__main__':
    tim = Account("Tim", 0)
    tim.show_balance()
    tim.deposit(1000)
    tim.withdraw(500)

    tim.withdraw(2000)
