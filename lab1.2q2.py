list1=[]
n=int(input("enter the number of elements :"))
print ("enter the elements :")
for i in range(0,n):
    no=int(input())
    if(no>100):
        list1.append("over")
    else:
        list1.append(no)
print(list1)