def nod(a,b):
    if a!=0 and b!=0:
        if a>b:
            return nod(a%b,b)
        else:
            return nod(a , b % a)
    if a==0:
        return b
    else:
        return a

a,b=map(int,input().split())
print(nod(a,b))