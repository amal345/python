str=input("enter the string:")
d1={}
for i in str:
    for letter in i:
        s=d1.keys()
        if  letter in s:
            d1[letter]=d1[letter]+1
        else:
            d1[letter]=1
print("character frequency=",d1)
