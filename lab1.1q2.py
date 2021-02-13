list=[]
n=int(input("Enter the no:of elements:"))
print("enter he elemnts")
for i in range (0,n):
    list.append(int(input()))
print("Elements in the list=",list)
print("positive integers are in the list:")
for i in list:
    if(i>0):
        print(i)