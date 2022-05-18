num1=int(input("Please input first number: "))
num2=int(input("Please input second number: "))

while(num1<=num2):

    if(num1 %2 !=0): #checks if the number is odd
        if(num1 == num2 or num1 == (num2-1)): #20
            print(str(num1)+"" ,end="")
        else:
            print(str(num1)+"," ,end="")

    
    num1=num1+1