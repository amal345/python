def count(str):
    words=[]
    words= str.split()
    counts=dict()
    for i in words:
        if i in counts:
            counts[i]=counts[i]+1
        else:
            counts[i]=1
    return counts
str=input("enter the string : ")
print(count(str))