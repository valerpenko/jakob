def isqrt1(a):
    x=a
    while True:
        x1=(x*x+a)//(2*x)
        if x1>=x: return x
        x=x1
def faktor(a):
    x=isqrt1(a)
    while True:
        x+=1
        z=x*x-a
        c=isqrt1(z)
        r=z-c*c
        if r==0:return (x-c,x+c)
print(faktor(int(input())))