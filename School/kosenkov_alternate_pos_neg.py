def alternate_pos_neg(a):
    otr=0
    pol=0
    for el in a:
        if otr>=2 or pol>=2:
            return False
        elif el < 0:
            otr+=1
            pol=0
        elif el>0:
            pol+=1
            otr=0
        else:
            return False
    return True

