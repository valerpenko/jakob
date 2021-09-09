import math
k1=1
for a in range(1,32767):
    for b in range(a,32767):
       d=a**2+b**2
       d=d**0.5
       if d==math.trunc(d):
           print(a,b,int(d),end="   ")
           k1+=1
           if k1%10==0:
                     print()

print(k1)