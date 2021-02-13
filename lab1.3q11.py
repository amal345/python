def gcd(n1,n2):
    i=1
    while(i<=n1 and i<=n2):
        if(n1%i==0 and n2%i==0):
            g=i
        i=i+1
    return g
n1=int(input("enter the first number:"))
n2=int(input("enter the second element: "))
print("gcd of",n1,"and",n2,"=",gcd(n1,n2))