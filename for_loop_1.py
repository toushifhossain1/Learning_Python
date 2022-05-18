# use continue for if condition , use pass for forLoop : ig you want to keep the contidion empty


for i in range(3):
    print(i)

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
    print("It did not pass")
  print(x)