def my_find(str):
    sep=[".","!","?"]
    i0 = str.find(sep[0])
    i1 = str.find(sep[1])
    i2 = str.find(sep[2])
    if i0==-1:
        i0=260
    if i1 == -1:
        i1 = 260
    if i2==-1:
        i2=260
    m=min([i0,i1,i2])
    return m+2
str=input()+" "
str=str.replace("...",".")
k=0
p=my_find(str)
while str!="":
    k+=1
    str=str[p:]
    p = my_find(str)
print(k)