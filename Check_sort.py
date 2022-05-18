def my_function(list):
    i = 0
    while i < 10:
        list.append(int(input("Enter the number")))
        i = i+1


def check_function(list):

    i = 0
    while i < len(list):
        if i == (len(list)-1):

            break

        elif(list[i] < list[i+1]):

            print(end="")

        else:
            print("not sorted")
            return

        i = i+1
    print("Sorted")


def find_max(list):
    i = 0
    temp = (list[0])
    while(i < len(list)):
        if(temp < list[i]):
            temp = list[i]
        else:
            print(end="")
        i = i+1
    print(temp)


def find_min(list):
    i = 0
    temp = (list[0])
    while(i < len(list)):
        if(temp > list[i]):
            temp = list[i]
        else:
            print(end="")
        i = i+1
    print(temp)


list = []

my_function(list)
# check_function(list)
# find_max(list)
find_min(list)
