word=input("enter the word:")
letters=list(word)
print("Alphabet : Ordinal Values:")
for i in letters:
    print(i,":",ord(i))