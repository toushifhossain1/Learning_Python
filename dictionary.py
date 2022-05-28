# The difference between a List and Dictionary is the Keys of the list are 0,1,2,3 and the keys of the Dictionary is defined by us

# here the Dictionary is a Phonebook and the Names are key and Numbers are value

PhoneBook = {
    "Toushif": [1621, 1731],
    "Sarwar": 1713
}

# if there is no match in the key (first parametre passed) then the second parametre will be executed

# it will return the second "Not in the phonebook"
PhoneBook.get("Peash", "Not in the phonebook")
print(PhoneBook.get("Peash", "Not in the phonebook"))

# Delete data from dictionary
del PhoneBook['Sarwar']
print(PhoneBook)

# converting Dictionary using list
keys = ["Java", "C++", "Python"]
values = ["Ecliple", "Atom", "Pycharm"]

ideForLang = dict(zip(keys, values))
print("List as a dictionary: ")
print(ideForLang)

# Access values from a dictionary
# Use the key to access the values
print(PhoneBook["Toushif"])
