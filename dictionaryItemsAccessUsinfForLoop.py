thisdict = {
    "key1": "value1",
    "key2": "value2"
}


# to printall the key items one by one
for x in thisdict:
    print(x)

# to print all the value items one by one
for x in thisdict:
    print(thisdict[x])

# to print keys and values

for x, y in thisdict.items():
    print(x, y)
