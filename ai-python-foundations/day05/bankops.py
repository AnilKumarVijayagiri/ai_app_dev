from datetime import datetime
class BankAccount:
    def __init__(self, acc_holder,balance):
        self.acc_holder = acc_holder
        self.balance = balance
    def get_transaction_time(self):
        return datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    def deposit(self, amount):
        self.balance += amount
        print("Amount deposited:", amount)
        print("Transaction time:", self.get_transaction_time())
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Amount withdrawn:", amount)
            print("Transaction time:", self.get_transaction_time())
        else:
            print("Insufficient balance.")
    def check_balance(self):
        print("Account holder:", self.acc_holder)
        print("Current balance:", self.balance)
        print("Transaction time:", self.get_transaction_time())
acc1 = BankAccount("Anil", 1000)
acc1.check_balance()
acc1.deposit(500)
acc1.check_balance()
acc1.withdraw(200)
acc1.check_balance()