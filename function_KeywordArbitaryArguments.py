# You can also send arguments with the key = value syntax.

# This way the order of the arguments does not matter.

# even though child3 was supposed to get the value "Emil" but it doesn't
def my_function(child3, child2, child1):

    print("The youngest child is " + child3)


my_function(child1="Emil", child2="Tobias", child3="Linus")
