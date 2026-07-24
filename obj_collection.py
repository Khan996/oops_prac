class Customer:

    def __init__(self, name, age):
        self.name = name 
        self.age = age

    def intro(self):
        print(f"My name is {self.name} and I'm {self.age}")

c1 = Customer("John", 34)
c2 = Customer("Michael", 44)
c3 = Customer("Elle", 24)
c4 = Customer("Mari", 54)

L = [c1, c2, c3, c4]

for i in L:
    i.intro()