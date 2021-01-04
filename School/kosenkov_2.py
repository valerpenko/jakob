L=list(map(int,input().split()))

if sum(L)>2:
    print(len(L))
else:
    L.reverse()
    print(L.pop())
