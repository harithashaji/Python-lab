str=input("enter a string")
print("original string",str)
c=str[0]
str=str.replace(c,'$')
str=c+str[1:]
print(str)
