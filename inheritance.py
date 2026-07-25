# For basic understanding
class User:

    def login(self):
        return "Login"

    def register(self):
        return "register"

class Student(User):

    def enroll(self):
        return "Enroll"

    def review(self):
        return "review"

stu1 = Student()
print(stu1.login())
print(stu1.register())
print(stu1.enroll())
print(stu1.review())