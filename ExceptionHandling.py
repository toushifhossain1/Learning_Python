# The try block lets you test a block of code for errors.

# The except block lets you handle the error.

# The else block lets you execute code when there is no error.

# The finally block lets you execute code, regardless of the result of the try- and except blocks.


# x = 5
try:
    print(x)

except NameError:
    print("Something is not defined please check")
else:
    # This will not work as there is an error and handled
    print("The else block is working as there is no error to be handled")
finally:
    print("This is the finally block")  # This will work no matter what
