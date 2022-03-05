def length(i):
    i=0
    for word in li:
        if len(word)>i:
            i=len(word)
            print("The longest word is:",i)
li=[]
n=int(input("Enter the number of word:"))
print("Enter the word:")
for j in range(0,n):
    li.append(input())
length(li)

