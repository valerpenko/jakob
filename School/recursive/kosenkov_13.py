def gcd(a,b):
    if a<b:
        a,b=b,a
    if b>0:
        return gcd(b,a%b)
    else:
        return a
a,b=map(int,input().split())
print(a//gcd(a,b)*b)