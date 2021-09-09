n=int(input())
k=2
while  k!=n//2:
    if n%k==0:
        print(k,n//k)
        break
    k+=1
if k==n//2:
    print(1,n)