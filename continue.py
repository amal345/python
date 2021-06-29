def gcd(x,y):
    if(y==0):
        return x
    else:
        return gcd(y,x%y)
x=int(input("enter the first number:"))
y=int(input("enter the first number:"))
num=gcd(x,y)
print("gcd of",x,"&",y,"=",num)
