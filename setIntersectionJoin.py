# 1) The intersection_update() method will keep only the items that are present in both sets.
# 2) The intersection() method will return a new set, that only contains the items that are present in both sets.

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.intersection_update(y)  # This will keep the intersection items in x
# print(x)  # x is changed


x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.intersection(y)
# print(z)
# print(x)  # x is unchanged
