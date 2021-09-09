def nod(a,b):
    if a==0:
        return b
    elif b==0:
        return a
    elif a>b:
        return nod(a%b,b)
    elif b>a:
        return nod(a,b%a)
    else:
        return a
l=[]
a,b=map(int,input().split())
d=nod(a,b)
for x in range(0,10**9):
    y=(-a*x+d)/b
    if y==int(y):
        l.append((x,y))

A*d+B*d=d
B+A=1
#5 3  3 5  8 1