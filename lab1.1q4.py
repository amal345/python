word=input("enter the word:")
letters=list(word)
vowels=[]
print("Vowels i the word:")
for i in 'a','e','i','o','u':
    if i in letters:
        vowels.append(i)
print(vowels)