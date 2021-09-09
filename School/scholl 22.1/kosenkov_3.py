def bank(a,p,k=0):
    if a<1000000:
        k += 1
        return bank(a+a/100*p,p,k)
    else:
        return k
a,p=map(int,input().split())
print(bank(a,p))