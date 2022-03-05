dict1={"a":100,"b":200,"c":300}
dict2={"x":500,"y":600,"z":700}
print("dict1",dict1)
print("dict2",dict2)
dict=dict1.copy()
dict.update(dict2)

print("Merged dictionary:",dict)
