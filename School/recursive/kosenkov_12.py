def max_1(a):
    if  len(a)==1:
        return a[0]
    else:
        m=max_1(a[1:])
        if a[0]>m:
            return a[0]
        else:
            return m
a=tuple(map(int,input().split()))
print(max_1(a))
