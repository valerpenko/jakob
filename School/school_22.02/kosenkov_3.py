def list():
    n=31
    l = [True] * (n + 1)
    k = 2
    while k * k <= n:
        if l[k]:
            i = k * k
            while i <= n:
                l[i] = False
                i += k
        k += 1
    p = []
    for i in range(2, n + 1):
        if l[i]:
            p.append(i)
    return p
def prost(n):
    v=True
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            v=False
            return v
    return v
l=[]
for el in list():
    f = 2**el-1
    l.append(prost(f))
print(list())
print(l)

