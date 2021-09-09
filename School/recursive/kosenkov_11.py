def my_pow(a,n):
    if n==0:
        return 1
    else:
        return my_pow(a,n-1)*a
a,n=map(int,input().split())
print(my_pow(a,n))