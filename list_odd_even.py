def my_function(list):
    i=0
    while i<10:
        list.append(int(input("Please enter  the number:")))
        i=i+1

def odd_list(list,list_odd):
    i=0
    
    while(i<len(list)):
        if(list[i]%2 ==1):
            list_odd.append(list[i])

        i=i+1

def even_list(list,list_even):
    i=0
    
    while(i<len(list)):
        if(list[i]%2 ==0):
            list_even.append(list[i])

        i=i+1

def print_list(list):
    print(list)

    
list=[]
list_odd=[]
list_even=[]
my_function(list)
odd_list(list,list_odd)
even_list(list,list_even)
#print_list(list_even)