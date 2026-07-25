class Customer:

    def __init__(self, name, gender, address):
        self.name = name
        self.gender = gender
        self.address = address

    def edit_profile(self, new_name, new_city, new_pin, new_state):
         self.name = new_name
         self.address.change_address(new_city, new_pin, new_state)

    
class Address:

    def __init__(self, city, pincode, state):
        self.city = city
        self.pincode = pincode
        self.state = state

    def change_address(self, new_city, new_pin, new_state):
            self.city = new_city
            self.pincode = new_pin
            self.state = new_state

add = Address("New York", 2300, "NY")
cust = Customer("John", "Male", add)
cust.edit_profile("Michael", "Washignton DC", 2000, "DC")

cust.edit_profile("Babar", "Islamabad", 5000, "Federal")
print(cust.name)
print(cust.address.city)
print(cust.address.pincode)
print(cust.address.state)
# print(cust.address.city)
# print(cust.address.pincode)
# print(cust.gender)
# print(cust.name)
# print(cust.address.state)