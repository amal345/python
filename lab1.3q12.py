no=int(input("enter the no:of elements:"))
list1=[]
print("enter the elments")
for i in range(0,no):
    list1.append(int(input()))
list2=[]
for i in list1:
    if(i%2!=0):
        list2.append(i)
print("elemnts that are not even:",list2)