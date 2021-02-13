sum=0
list=[]
n=int(input("enter the no: of elements:"))
print("enter the elements:")
for i in range(0,n):
    list.append(int(input()))
for i in range(0,len(list)):
    sum=sum+list[i]
print("sum of elements in the list=",sum)