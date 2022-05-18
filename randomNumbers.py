# import random -> this imports the whole libnrary, most of which we donot need
from random import randint

randomNumber = randint(1, 5)
# print(randomNumber)

userInput = int(input("Please Enter any number from 1 to 5: "))

if userInput >= 1 and userInput <= 5:
    if randomNumber == userInput:
        print("The random number generated and user input is the same !!!")
    else:
        print("The random number generated and user input is not the same")
else:
    print("The input is not between 1 to 5")
