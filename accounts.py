import datetime
import pytz


class Account:
    """Simple account class with balance"""
    @staticmethod
    def _current_time():
        utc_time = datetime.datetime.utcnow()
        return pytz.utc.localize(utc_time)

    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance
        self.transaction_list = []
        self.transaction_list.append((Account._current_time(), balance))
        #self.deposit(balance)
        print("Account created for " + self.name)

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
        self.show_balance()
        self.transaction_list.append((Account._current_time(), amount))

    def withdraw(self, amount):
        if amount > 0:
            self.__balance -= amount
        self.show_balance()
        self.transaction_list.append((self._current_time(), -amount))

    def show_balance(self):
        print("Balance is {}".format(self.__balance))

    def show_transactions(self):
        for date, amount in self.transaction_list:
            if amount > 0:
                trans_type = "deposited"
            else:
                amount = amount * -1
                trans_type = "withdrawn"
            print("{:_>6d} {} on {} (local time was {})".format(amount, trans_type, date, date.astimezone()))


if __name__ == "__main__":
    # gagan = Account("Gagan", 1000)
    # # gagan.show_balance()
    # gagan.deposit(1000)
    # # gagan.show_balance()
    # gagan.withdraw(500)
    # # gagan.show_balance()
    # gagan.show_transactions()

    steph = Account("Steph", 800)
    steph.__balance = 200
    steph.show_balance()
    # print(steph.__dict__)
    # print(steph.__balance)
    # print(steph._Account__balance)
