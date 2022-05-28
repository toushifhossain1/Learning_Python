# is subset : Return True if all items in set x are present in set y, then x is a subset of y:

x = {"a", "b", "c"}
y = {"f", "e", "d", "c", "b", "a"}
c = {"x", "y", "z"}

z = x.issubset(y)

# print(z)

# is superset: Return True if all items set x are present in set y, then y is a superset of x:

z = y.issuperset(x)
# print(z)

# The isdisjoint() method returns True if none of the items are present in both sets, otherwise it returns False.

z = x.isdisjoint(c)
print(z)
