l=[3,4,5,3,9,10]
for i in range(len(l)-1):
    f=True
    for j in range(len(l)-i-1):
        print("*")
        if l[j]>l[j+1] :
            l[j],l[j+1]=l[j+1],l[j]
            f=False
    if f:
        break
print(l)