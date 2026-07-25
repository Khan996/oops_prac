# # For basic understanding
# class User:

#     def login(self):
#         return "Login"

#     def register(self):
#         return "register"

# class Student(User):

#     def enroll(self):
#         return "Enroll"

#     def review(self):
#         return "review"

# stu1 = Student()
# print(stu1.login())
# print(stu1.register())
# print(stu1.enroll())
# print(stu1.review())
#-----------------------------------
# Another basic example 
# class Phone:
#     def __init__(self, price, brand, camera):
#         print("Inside Phone Constructor")
#         self.price = price
#         self.brand = brand 
#         self.camera = camera 

# class SmartPhone(Phone):
#     pass

# s = SmartPhone(50000, "Iphone", "14")
# print(s.brand)
# print(s.price)
# print(s.camera)

# ---------------------------
# Overriding example 
class Phone:
    def __init__(self, price, brand, camera):
        print("Inside Phone Constructor")
        self.price = price
        self.brand = brand 
        self.camera = camera 

    def buy(self):
        print("Buy the phone")
class SmartPhone(Phone):

    def buy(self):
        print("Buy the smartphone")

s = SmartPhone(50000, "Iphone", "14")
print(s.brand)
print(s.price)
print(s.camera)
s.buy()