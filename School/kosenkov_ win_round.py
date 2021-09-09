def win_round(a,b):
    l1_max=[]
    l2_max=[]
    for i in range(8):
        if i <4:
            l1_max.append(a[i]*10+a[i+1])
        else:
            l1_max.append(a[5-i]*10+a[4-i])
    for i in range(8):
        if i <4:
            l2_max.append(b[i]*10+b[i+1])
        else:
            l2_max.append(b[5-i]*10+b[4-i])
    if max(l1_max)>max(l2_max):
        return True
    else:
        return False