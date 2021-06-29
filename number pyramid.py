"""n=int(input("enter the number:"))
for i in range(n,0,-1):
    for j in range(1,i):
        print(i*j,end="")
    print()
num=int(input("row="))
i=1
while i<=num:
    j=1
    while(j<=i):
        print("*",end=' ')
        j=j+1
    print(" ")
    i=i+1
i=num-1
while i>=0:
    j=1
    while(j<=i):
        print("*",end=' ')
        j=j+1
    print(" ")
    i=i-1"""
str=input("enter the string:")
w=str.split()
count={}
for i in w:
        for j in i:
            if j in count:
                count[j]=count[j]+1
            else:
                count[j]=1
print(count)
a=count.keys()
print(a)
