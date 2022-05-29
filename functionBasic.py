# In Python a function is defined using the def keyword:

def printFunction():
    print("Hello world")


# printFunction()

# A parameter is the variable listed inside the parentheses in the function definition.

# An argument is the value that is sent to the function when it is called.


def sumFunction(val1, val2):  # Here val1 and val2 are parameter
    sum = val1+val2
    print(sum)


# sumFunction(1, 2)  # here 1,2 are arguments

# In python you dont need to define whether the function will return or not in the declaration
# if you want to keep the function empty use the keyword " pass "

def returnSum(num1, num2):
    sum = num1+num2
    return sum


sumReturned = returnSum(2, 5)
print(sumReturned)


def functionDoesNothing():
    pass
