# If you do not know how many keyword arguments that will be passed into your function, add two asterisk: ** before the parameter name in the function definition.

# This way the function will receive a dictionary of arguments, and can access the items accordingly:


def my_function(**kid):
    # here the "lname" is the key of the dictionary kid
    print("His last name is " + kid["lname"])


my_function(fname="Tobias", lname="Refsnes")
