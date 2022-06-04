# polymorphism means the same function name but different defination
# Polymorphism lets us define methods in the child class that have the same name as the methods in the parent class
# This process of re-implementing a method in the child class is known as Method Overriding (Polymorphism).
# In c++ and JAVA it is written by @override but in python just write the function name and give different defination

# example without class and method:

# ---------------- using predefined function ----------------

# len() being used for a string
from abc import ABC, abstractmethod
print(len("geeks"))

# len() being used for a list
print(len([10, 20, 30]))

# ---------------- using user made function ----------------


def add(x, y, z=0):
    return x + y+z


# Driver code
print(add(2, 3))
print(add(2, 3, 4))


# example with class and method:


class shape (ABC):  # ABC is the abctract base class parameter
    def __init__(self, dim1, dim2):
        self.dim1 = dim1
        self.dim2 = dim2

    @abstractmethod
    def area(self):
        pass


class triangle(shape):
    # here the area methos is polymorphic method
    def area(self):
        area = 0.5 * self.dim1*self.dim2
        print("Area of the triangle= ", area)


class rectangle(shape):
    def area(self):
        area = self.dim1*self.dim2
        print("Area of the rectangle= ", area)

# The shape class cannot  be instantiated as it is an abstract class
# shape1 = shape()


triangle1 = triangle(10, 20)
triangle1.area()
rectangle1 = rectangle(10, 20)
rectangle1.area()
