n=int(input("enter the number:"))
fact=1
if(n==0):
    fact=1
elif(n<0):
    print("can't find factorial of negative number")
else:
    for i in range(1,n+1):
        fact=fact*i
    print("facorial of",n,"=",fact)