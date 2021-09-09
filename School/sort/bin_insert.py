l1=[3,11,10,3]
l=[l1.pop(0)]

while len(l1)>0:

    nomer_lev = 0
    nomer_prav = len(l)-1
    while nomer_lev>nomer_prav:
        nomer_sred = (nomer_lev +nomer_prav)//2
        if l1[0]==l[nomer_sred]:
            l.insert(nomer_sred,l1[0])
            break
        elif l1[0]>l[nomer_sred]:
            nomer_lev=nomer_sred
        else:
            nomer_prav=nomer_sred
