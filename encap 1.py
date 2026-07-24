class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.__salary = salary
        
    def get_salary(self):
        if self.__salary <= 0:
            return False
        return self.__salary
            

    def set_salary(self, salary):
        self.__salary = salary


emp = Employee("John", -50000)
emp.get_salary()
print("It prints False bz salary is neg: ",emp.get_salary())

emp.set_salary(45000)
print("It prints 45 thousands salary: ", emp.get_salary())

emp.set_salary(-89000)
print("It prints False bz salary is neg: ", emp.get_salary())

emp.set_salary(79000)
print("it print 79 thousands", emp.get_salary())

#print(emp.__salary) # it gives attribute error python does not 
# allow direct access to __salary because it is private, so we 
# create a getter 

print(emp.get_salary()) # it prints the salary what is previously
# stored. 

emp.__salary = -90000 # Suppose we do not have a setter 
print(emp.get_salary())
