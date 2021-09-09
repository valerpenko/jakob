def sum (a,b,c,d):
    y=b*d
    x=a*d+b*c
    k=nok(x,y)
    x=x/k
    y=y/k
    return x,y
def mult(a, b, c, d):
    x=a*c
    y=b*d
    k=nok(x,y)
    x=x/k
    y=y/k
    return x, y
def nok(x,y):
    #алгоритм эвклида сделать самому
    return a,b
try:
    a,b,c,d=map(int,input().split())
    x,y=sum(a,b,c,d)
    print(x,"/",y)
    x, y = sum(a, b, -c, d)
    print(x, "/", y)
    x, y =mult(a, b, c, d)
    print(x, "/", y)
    x, y = mult(a, b, d, c)
    print(x, "/", y)
except ValueError:
    print("печатайте акуратнее")
except ZeroDivisionError:
    print("на ноль делить нельзя")