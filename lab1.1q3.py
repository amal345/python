list=[]
n=int(input("Enter the no:of elements:"))
print("enter he elemnts")
for i in range (0,n):
    list.append(int(input()))
print("Elements in the list1=",list)
square=[]
for i in list:
    sq=i*i
    square.append(sq)
print("square of elements in list1 is:",square)