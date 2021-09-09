l1=[3,11,10,3]
l=[l1.pop(0)]
while len(l1)>0:
    f=True
    for i in range(len(l)):
        if l1[0]<l[i]:
            l.insert(i,l1.pop(0))
            f=False
            break
    if  f:
        l.append(l1.pop(0))

print(l)
