string=input("enter a string : ")
first=string[0]
string1=string.replace(first,'$')
word=first+string1[1:]
print(word)