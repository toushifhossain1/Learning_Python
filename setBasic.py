# A set is a collection which is unordered, unchangeable* ( But new items can be added and removed ), and unindexed

mySet = {"value1", 2, "string", 3.14}
myList = list(("first", "second"))
#mySet = set(("value1", 2, "string", 3.14))

# print(type(mySet))

# To add one item to a set use the add() method.
mySet.add("something")

# The object in the update() method does not have to be a set, it can be any iterable object (tuples, lists, dictionaries etc.).

mySet.update(myList)

# both remove() and discard() can be used to remove value;
# If the item to remove does not exist, remove() will raise an error.
# If the item to remove does not exist, discard() will NOT raise an error.

mySet.discard(2)

# we can also use the pop() method to return and remove an item ( as sets are unodered so any item will be returned and removed)
removed = mySet.pop()

print("The popped item is " + str(removed))
# the only way to access the elements inside a set is to loop through the set

for x in mySet:
    print(x)

# the differnce between del and clear is del also removes the identity of the set but clear only clears the items inside
mySet.clear()
print(type(mySet))


del mySet
print(type(mySet))
