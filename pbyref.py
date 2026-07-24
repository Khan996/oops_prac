# class Customer:

#     def __init__(self, name, gender):
#         self.name = name 
#         self.gender = gender

# def greet(customer):
#     if customer.gender == "Male":
#         print(f"Hello {customer.name} Sir")
#     else:
#         print(f"Hello {customer.name} Ma'am")

#     cust2 = Customer("John", "male")
#     return cust2

# cust = Customer("Natasha", "Female")
# # greet(cust)
# new_cust = greet(cust)
# print(new_cust.name)
# print(cust.name)
# print(cust.gender)

class Customer:

    def __init__(self, name):
        self.name = name

def greet(Customer):
    # print("the customer id is: ",id(Customer))
    print("The id of Babar is: ", id(Customer.name))
    Customer.name = "John"
    print(f"The customer name is: {Customer.name}")
    print("The id of John is: ", id(Customer.name))

cust =  Customer("Babar")
print("The id of Babar is: ", id(cust.name))
# print("the cust id is: ",id(cust))
greet(cust)
print(cust.name)
print("The id of John is: ", id(cust.name))