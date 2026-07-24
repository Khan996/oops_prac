class Student:

    def __init__(self, name, marks, rollNumber):

        self.name = name
        self.marks = marks 
        self.rollNumber = rollNumber 

    def study(self):
        print(f"{self.name} is studying")

    def play(self):
        print(f"{self.name} is playing")


s1 = Student("Mike", "78", "123")
s2 = Student("John", "85","2345")
s1.study()
s1.play()
s2.study()
s2.play()
print(s1.name, s1.marks, s1.rollNumber)
print(s2.name, s2.marks, s2.rollNumber)