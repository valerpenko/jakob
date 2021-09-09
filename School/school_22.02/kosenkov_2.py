import math

n=int(input())
l=[True]*(n+1)
k=2
while k*k<=n:
    if l[k]:
        i=k*k
        while i <=n:
            l[i]=False
            i+=k
    k+=1
for i in range(2,n+1):
    if l[i]:
        print(i)