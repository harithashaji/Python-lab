def longestLength(a):
    max1 = len(a[0])
    temp = a[0]
    for i in a:
        if (len(i) > max1):
            max1 = len(i)
            temp = i
    print("The word with the longest length is:", temp,
          "\n and length is ", max1)
a = ["apple", "orange", "jackfruit", "grapes"]
longestLength(a)