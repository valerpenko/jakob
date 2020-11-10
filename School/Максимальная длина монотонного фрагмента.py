new=int(input())
k=0
k_max=k
old=new
grow=0
while new!=0:
    if new>old :
        if grow==1:
            k+=1
            if k>k_max:
                k_max=k
        else:
            grow=1
            k=1
            if k>k_max:
                k_max=k
    elif new<old:
        if grow==-1:
            k+=1
            if k>k_max:
                k_max=k
        else:
            grow = -1
            k = 1
            if k > k_max:
                k_max = k
    else:
        k=1
        grow=0
    new=int(input())
print(k_max)