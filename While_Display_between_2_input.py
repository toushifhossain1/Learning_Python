num1= int(input("Enter the first number:")) #5
num2 = int( input("Enter the second number:")) #10

while(num1<=num2):
    if(num1 != num2): 
            print(str(num1) + ", " ,end= "")
    else:
            print(str(num1),end= "")
    num1=num1+1 