def sum_square(n,m):
    if n == m :
        return m**2
    else:
        return sum_square(n,m-1)+m**2
n,m=map(int,input().split())
print(sum_square(n,m))