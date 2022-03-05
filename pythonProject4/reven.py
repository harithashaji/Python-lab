n=int(input("Enter the limit:"))
list=[]
print("Enter the elements:")
for i in range(0,n):
    n=int(input())
    list.append(n)
leven=[]
lodd=[]
for i in list:
    if(i%2)==0:
        leven.append(i)
    else:
        lodd.append(i)
print(lodd)





