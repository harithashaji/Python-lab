str1=input("Enter a string")
str1=str1.lower()
str2=set(str1)
print("characters and its count are:")
for i in str2:
    c=0
    for j in range(0,len(str1)):
        if i==str[j]:
            c+=1
    print(i":"c)


