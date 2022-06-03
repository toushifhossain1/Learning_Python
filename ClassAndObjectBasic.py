
class student:
    name = ""
    gpa = ""

# self is the this pointer in python
# The self parameter is a reference to the current instance of the class, and is used to access variables that belongs to the class.
# __init__ is the constructor in python

    def __init__(self, name, gpa) -> None:
        self.name = name
        self.gpa = gpa

    def display(self):
        print(self.name, self.gpa)


student1 = student("Toushif", "3")

# print("Student name= " + student1.name, "and his gpa= " + student1.gpa)
# student1.display()
