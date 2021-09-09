n=int(input())
l=list(map(int, input().split()))
s=[]
for i in range(len(l)):
    try:
        if l.index(l[i],i+1)!=1:
            if l[i] not in s:
                s.append(l[i])
    except ValueError:
        pass
if s:
    for el in s:
        print(el,end=" ")
else:
    print("NO")