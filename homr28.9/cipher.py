import math
a=input()
t=0
S1=""
S2=""
if len(a)%2==0:
    for i in range(0,len(a)//2):
        S1=S1+a[i+t]
        S2=S2+a[i+1+t]
        t=t+1
else:
    S1 = S1 + a[0 + t]
    for i in range(0, len(a) // 2):
        S2 = S2 + a[i + 1 + t]
        S1 = S1 + a[i + t+2]
        t=t+1
S1=S1[::-1]
SQ=S1+S2
print(S1,S2,SQ)
S_long=math.ceil(len(SQ)/2)
# S_long=int(len(SQ))//2
# if len(SQ)%2==1:
#     S_long+=1
A1=SQ[0:S_long]
A2=SQ[S_long:]
A1=A1[::-1]
S_First=""
for i in range(0,len(A2)):
    S_First+=A1[i]+A2[i]
if len(SQ)%2==1:
    S_First+=A1[len(A1)-1]

print(A1, A2)
print(S_First)
