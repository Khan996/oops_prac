class Atm:

    def __init__(self, owner, balance):
        self.__owner = owner
        self.__balance = balance
        self.__pin = 0
        #self.menu()

    def start(self):
        self.__menu()

    def get_pin(self):
        return self.__pin

    def set_pin(self, new_pin):
        if type(new_pin) == str:
            self.__pin = new_pin
            print("Pin changed")
        else:
            print("Not allowed")

    def __menu(self):
        user_input = input (f"""Hello, Welcome {self.__owner} how do you want to proced?
                1. Enter 1 to create pin?
                2. Enter 2 to make a deposit.
                3. Enter 3 to withdraw money.
                4. Enter 4 to check balance.
                5. Enter 5 to exit        
                """)
        if user_input == "1":
            self.create_pin()
        elif user_input == "2":
            self.deposit()
        elif user_input == "3":
            self.withdraw()
        elif user_input == "4":
            self.check_balance()
        else:
            print("bye")

    def create_pin(self):
        self.__pin = int(input("Enter your pin "))
        print("Pin created successfully")
        self.__menu()

    def deposit(self):
        temp = int(input("Enter your pin "))
        if temp == self.__pin:
            amount = int(input("Enter the amount "))
            self.__balance = self.__balance + amount
            print(f"Deposit successful and the balance is {self.__balance}")
        else:
            print("invalid pin")
        self.__menu()

    def withdraw(self):
        temp = int(input("Enter your pin "))
        if temp == self.__pin:
            amount = int(input("Enter the amount "))
            if amount < self.__balance:
                self.__balance = self.__balance - amount 
                print(f"Operation successful and the balance is {self.__balance}")
            else:
                print("insufficient funds ")
        else:
            print("invalid pin")
        self.__menu()

    def check_balance(self):
        temp = int(input("Enter your pin "))
        if temp == self.__pin:
            print(self.__balance)
        else:
            print("invalid pin")
        self.__menu()

    def show(self):
        print(self.__balance)  

# a =  Atm("Ali", 50000)
# b = Atm("Babar", 20000)
# c = Atm("Jawad", 4000)
# d = Atm("Ahmed", 250000)

# a.start()
# b.start()
# c.start()
# d.start()