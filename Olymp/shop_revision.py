
r1,k1,r2,k2=map(int,input().split())
list=[]
for l in range(1,203):
    price=r1*100+k1
    rest=r2*100+k2
    s=(l*price-rest)/1000
    if s==int(s):
        list.append((l,int(s)))
if len(list)==1:
    print(list[0][0],list[0][1]*10+r2,k2)
elif len(list)==0:
    print(-1)
elif len(list)>1:
    print("O-o-ops!")