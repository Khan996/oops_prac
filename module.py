from atm import Atm

a = Atm("Ali", 5000)
# print(a._Atm__balance)
# a.get_pin()
# a.start()
print(a.get_pin())
a.set_pin("123")
a.start()

# a.__menu()

# 
# a.start()
# a.menu()
# print()
# print()

# class Atm:

#     def __init__(self, owner, balance):
#         self.owner = owner
#         self.balance = balance
#         self.pin = 0
#         #self.menu()

#     def start(self):
#         self.menu()

#     def menu(self):
#         user_input = input (f"""Hello, Welcome {self.owner} how do you want to proced?
#                 1. Enter 1 to create pin?
#                 2. Enter 2 to make a deposit.
#                 3. Enter 3 to withdraw money.
#                 4. Enter 4 to check balance.
#                 5. Enter 5 to exit        
#                 """)
#         if user_input == "1":
#             self.create_pin()
#         elif user_input == "2":
#             self.deposit()
#         elif user_input == "3":
#             self.withdraw()
#         elif user_input == "4":
#             self.check_balance()
#         else:
#             print("bye")

#     def create_pin(self):
#         self.pin = int(input("Enter your pin "))
#         print("Pin created successfully")
#         self.menu()

#     def deposit(self):
#         temp = int(input("Enter your pin "))
#         if temp == self.pin:
#             amount = int(input("Enter the amount "))
#             self.balance = self.balance + amount
#             print(f"Deposit successful and the balance is {self.balance}")
#         else:
#             print("invalid pin")
#         self.menu()

#     def withdraw(self):
#         temp = int(input("Enter your pin "))
#         if temp == self.pin:
#             amount = int(input("Enter the amount "))
#             if amount < self.balance:
#                 self.balance = self.balance - amount 
#                 print(f"Operation successful and the balance is {self.balance}")
#             else:
#                 print("insufficient funds ")
#         else:
#             print("invalid pin")
#         self.menu()

#     def check_balance(self):
#         temp = int(input("Enter your pin "))
#         if temp == self.pin:
#             print(self.balance)
#         else:
#             print("invalid pin")
#         self.menu()

#     def show(self):
#         print(self.balance)  

# a =  Atm("Ali", 50000)
# a.menu()
# print(a.balance)
# print(a.owner)

