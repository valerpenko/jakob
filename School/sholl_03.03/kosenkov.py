import math
def isqrt(a):
    x=a
    while True:
        x1=(x*x+a)//(2*x)
        if x1>=x: return x
        x=x1
b1=True
c1=True
a1=True

b=True
c=True
a=True
k=1000000000000000
while a==True or b==True or c==True:
    if k!=(k*k)**0.5:
        a=False
        if a1==True:
            print("0.5",k)
            a1=False
    if k != math.sqrt(k * k) :
        b = False
        if b1==True:
            print("math.sqrt",k)
            b1=False
    if k != isqrt(k * k) :
        c=False
        if c1==True:
            print("isqrt",k)
            c1=False
    k+=1
