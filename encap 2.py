class BankAccount():

    def __init__(self):
        self.__balance = 8000

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"You have deposited it :{amount}")

    def withdrew(self, amount):
        if amount <= self.__balance and amount > 0:
            self.__balance -= amount
            print(f"You have withdrawn: {amount}")

    def get_balance(self):
        return self.__balance

acc = BankAccount()
print(f"Your bank balance currenty is: {acc.get_balance()} " )
acc.deposit(1000)
print("Your balance becomes: ", acc.get_balance())
acc.withdrew(200)
print("You have withdrawn, so your balance becomes: ", acc.get_balance())
print("Your current balance is: ", acc.get_balance())