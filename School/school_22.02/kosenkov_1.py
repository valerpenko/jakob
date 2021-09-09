def prost(n):
    v=True
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            v=False
            return v
    return v
print(prost(int(input())))