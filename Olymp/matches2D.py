import math
n=int(input())
def am(k,a):
    if a<=k:
        return 3+(k-1)*2
    else:
        return 6+(k-2)*2
k=math.floor(n**0.5)
if k**2<n<(k+1)**2:
    a=n-k**2
    full=am(k,a)+2*k*(k+1)
    print(full)
else:
 print(2*k*(k+1))
