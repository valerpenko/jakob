s=int(input())
for m in range(1,13):
    d=(s-m*31)/12
    if d==int(d):
        if d<10:
            print("0"+str(int(d)),end="/")
        else:
            print(str(int(d)), end="/")
        if m<10:
            print("0" + str(m))
        else:
            print(str(m))