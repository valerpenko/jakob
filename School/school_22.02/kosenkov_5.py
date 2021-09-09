def aftomorph(n):
    k=n*n
    if 1 <=n<10:
        if k%10==n:
            return True
    elif 10 <= n < 100:
        if k % 100 == n:
            return True
    elif 100 <=n<1000:
        if k%1000==n:
            return True
    else:
        return False
for i in range(1,999):
    if i%10==1 or i%10==5 or i%10==6:
        if aftomorph(i):
            print(i,end=" ")