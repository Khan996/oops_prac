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
# class Phone:
#     def __init__(self, price, brand, camera):
#         print("Inside Phone Constructor")
#         self.price = price
#         self.brand = brand 
#         self.camera = camera 

#     def buy(self):
#         print("Buy the phone")
# class SmartPhone(Phone):

#     def buy(self):
#         print("Buy the smartphone")

# s = SmartPhone(50000, "Iphone", "14")
# print(s.brand)
# print(s.price)
# print(s.camera)
# s.buy()
#--------------------------
# Child-Parent Example
# class Parent:

#     def __init__(self, num):
#         self.num = num

#     def get_num(self):
#         return self.num
    
# class Child(Parent):

#     def show(self):
#         print("This is in child class")
    
# c = Child(100)
# print(c.get_num())
# c.show()
#-------------------------------------------
# Child-Parent Example
# class Parent:

#     def __init__(self, num):
#         self.__num = num

#     def get_num(self):
#         return self.__num
    
# class Child(Parent):

#     def __init__(self, val, num):
#         self.__val = val

#     def get_val(self):
#         return self.__val
    
# c = Child(100, 10)
# print(c.get_num())
#---------------------------------------
class A:

    def __init__(self):
        self.num = 100

    def display1(self,num):
        print(f"Class A: {self.num}")

class B(A):

    def display2(self, num):
        print(f"Class B: {self.num}")

s = B()
s.display1(1000)
s.display2(28)