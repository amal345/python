def fun_string(str1):
 length = len(str1)
 if length > 2:
    if str1[-3:] == 'ing':
        str1 = str1 + 'ly'
    else:
        str1 = str1 + 'ing'
 print ("Modified string: ",str1)
str1=input("Enter a string:")
fun_string(str1)
