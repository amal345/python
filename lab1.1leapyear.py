cr=int(input("enter the current year:"))
fr=int(input("enter the final year:"))
for i in range(cr,fr+1):
    if((i%4==0 and i%100!=0) or i%400==0):
        print("leap years are: ",i)