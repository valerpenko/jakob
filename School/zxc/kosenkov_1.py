import math
def factor(g):
    a=[1]
    for k in range(2,g+1):
        r=0
        d=1000000
        for i in range(len(a)):
            s=a[i]*k+r
            a[i]=s%d
            r=s//d
        if r>0:
            a.append(r)
    return a
a=factor(int(input()))

b=""
h=len(a)
for i in range(h-1,-1,-1):
    b+="{:06d}".format(a[i])
print(b[4:])
m=math.factorial(100)
print(int(b)==m)