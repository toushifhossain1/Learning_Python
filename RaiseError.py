# As a Python developer you can choose to throw an exception if a condition occurs.

# To throw (or raise) an exception, use the raise keyword.

x = int(input("Please input a number greater then 0: "))

if x < 0:
    raise Exception("Sorry, no numbers below zero")
