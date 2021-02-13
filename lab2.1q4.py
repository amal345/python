import math
n=int(input("enter the lower bound:"))
m=int(input("enter the upper bound:"))
list=[]
for i in range(n,m+1):
    count=flag=0
    num=str(i)
    for j in num:
        count=count+1
        if int(j)%2!=0:
            flag=1
    if (count==4 and int(num)==(math.isqrt(int(num))**2) and flag==0):
        list.append(int(num))
if(len(list)==0):
    print("list is empty")
else:
    print("resultant list is:",list)