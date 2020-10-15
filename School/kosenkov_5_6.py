S=input()
sim=S[0]
k=1
rez=""
for i in range(1,len(S)):
    if sim==S[i]:
        k+=1
    else:
        rez=rez+sim+str(k)
        k=1
        sim=S[i]
rez = rez + sim + str(k)
print(rez)
S2=""
count=""
sim=rez[0]
for i in range(1,len(rez)):
    if rez[i].isdigit():
        count=count+rez[i]
    else:
        S2 =S2+sim*int(count)
        count=""
        sim=rez[i]
S2 =S2+sim*int(count)
print(S2)