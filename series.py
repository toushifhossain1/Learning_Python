# 1+2+3+4+...+n
n = int(input("Please enter the last digit of the series: "))

# sum of n using while loop:
i=0
sum=0
while i<=n:
    sum=sum+i
    i=i+1
print("Print sum using while : " + str(sum))
sum=0
# sum of n using for loop:
for i in range(n+1): #n+1 because the loop will run <n not = n
    sum=sum+i
print("Print sum using for : " + str(sum))



# 1*1 + 2*2 + 3*3 + 4*4 + 5*5 + 6*6 ... n*n'

#using while loop
mult = 1 
i=1
while i<=n:
    mult = mult*i
    i=i+1
print("Mult up to n using while " + str(mult))

#using for loop
mult =1
for i in range(1,n+1):
    mult = mult*i
    
print("Mult up to n using for " + str(mult))