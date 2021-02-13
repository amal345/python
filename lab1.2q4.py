list1=[1,2,3,5,6]
list2=[6,7,8,9,10]
count=0
if(len(list1)==len(list2)):
    print("The two list are in same length.")
else:
    print("The two list are not in same lemgth")
if(sum(list1)==sum(list2)):
    print("The two list have same sum of values.")
else:
    print("The two list are not have same sum values")
out=any(check in list2 for check in list1)
print("common values",out)
a=set(list1).intersection(set(list2))
print("The common value=",a)