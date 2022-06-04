# An abstract method is a method that is declared, but contains no implementation, the implementation is overriden by the inherited class
# there must be a notation " @abstractmethod " placed before writing the method
# A class is called an Abstract class if it contains one or more abstract methods.
# Abstract class cannot be used as a object, abstract method must be overriden to use

from abc import ABC, abstractmethod


class shape (ABC):  # ABC is the abctract class parameter
    def __init__(self, dim1, dim2):
        self.dim1 = dim1
        self.dim2 = dim2

    @abstractmethod
    def area(self):
        pass


class triangle(shape):
    def area(self):
        area = 0.5 * self.dim1*self.dim2
        print("Area of the triangle= ", area)


# The shape class cannot  be instantiated as it is an abstract class
# shape1 = shape()

triangle1 = triangle(10, 20)
triangle1.area()
