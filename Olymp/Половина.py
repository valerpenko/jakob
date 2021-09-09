n=int(input())
mart=[]
for i in range(n):
    line=[]
    for j in range(n):
        if j+i+1<n:
            line.append(2)
        elif i+j+1==n:
            line.append(0)
        else:
            line.append(1)
    mart.extend(line)

for el in mart:
    for i in el:
        print(i, end="")
    print()