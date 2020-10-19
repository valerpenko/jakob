# a = int(input("a:"))
# b = int(input("b:"))
# c = int(input("c:"))

s=input("Type a,b,c: ")
abc=s.split(' ')
a=int(abc[0])
b=int(abc[1])
c=int(abc[2])

if a>c+b :
    print("error")
else:
    if b > c + a :
        print("error")
    else:
        if c > b + a :
            print("error")
        else:
            print("ok")

if a>c+b or b > c + a or c > b + a:
    print("error")
else:
    print("ok")