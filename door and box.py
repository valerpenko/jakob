a,b,c,m,k=map(int,input().split())
if a>b:
    if a>c:
        x=c
        y=b
    else:
        x=a
        y=b
else:
    if b>c:
        x=c
        y=a
    else:
        x=b
        y=a
if m<k:
    m,k=k,m
if x<y:
    x,y=y,x
if m>x and k>y :
    print('yes')
else:
    print("no")