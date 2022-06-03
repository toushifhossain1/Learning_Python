# Inheritance allows us to define a class that inherits all the methods and properties from another class.

# Parent class is the class being inherited from, also called base class.

# Child class is the class that inherits from another class, also called derived class.


# here phone is the parent (super/base) class
class Phone:
    def call(self):
        print("you can call")

    def message(self):
        print("you can message")


# samsung is the sub (child/derived) class
class Samsung(Phone):
    def photo(self):
        print("you can take photo")


A320 = Samsung()
A320.call()

# to check for subclass
print(issubclass(Samsung, Phone))
