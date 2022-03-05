list=[]
n=int(input("enter the limit:"))
print("Enter the values:")
for i in range(0,n):
    ele=int(input())
    list.append(ele)
print(list)
result=[]
for i in list:
    if i>100:
        result.append("over")
    else:
        result.append(i)
print(result)