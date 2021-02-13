n=int(input("enter the number:"))
a=0
b=1
if(n<=0):
    print("Term should be positive number")
elif(n==1):
    print("fibinacci series=",a )
elif (n == 2):
    print("fibinacci series=", a,b)
else:
    print("fibinacci series=",a,b,"\t",end='')
    for i in range(2,n):
        c=a+b
        a=b
        b=c
        print(c,"\t",end='')