# sets can be joined in two ways
# 1) using the union() method: this method joins two sets and returns the new set ( join will exculde duplicates)
# 2) using update() method: this will join the passed parametered set into the method called set
#    for example set1.update(set2); set 2 will remain same but set 1 will be updated

# 1) Using union method
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
# print(set3)

# 2) using update method

set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set1.update(set2)
print(set1)
