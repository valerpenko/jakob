def f(x,i=0):
    i+=1
    if i == x:
        return x
    if i < x:
        return f((x//i)**i,i)




x=int(input())
print(f(x))