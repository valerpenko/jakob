objects = [1, 2.6, "Hello", True,46]
s=0
for el in objects:
    if type(el) is int or type(el) is float:
        s+=el
print(s)