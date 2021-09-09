def f(m,n):
    if m==0 or n==0:
        if m==0:
            return n
        else:
            return m
    else:
        if m>n:
            return f(m%n,n)
        else:
            return f(n%m,m)
m,n=map(int,input().split())
print(f(m,n))