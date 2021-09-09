def fakt_2(n):
    if n%2==0:
        if n==2:
            return 2
        else:
            return fakt_2(n-2)*n
    else:
        if n==1:
            return 1
        else:
            return fakt_2(n-2)*n
n=int(input())
print(fakt_2(n))