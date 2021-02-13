list=['anu','abhijith','binu','lekshmi','reshma']
count=0
for i in list:
    for j in i:
        if j=='a':
            count=count+1
print("The List is",list)
print(" number of time a occured:", count)