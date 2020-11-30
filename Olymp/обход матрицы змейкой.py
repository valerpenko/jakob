n=int(input())
matrix=[]
for i in range(n):
    line=[]
    for j in range(n):
        line.append(i*n+j+1)
    if i%2!=0:
        line=line[::-1]
    matrix.append(line)
for el in matrix:
    for el1 in el:
        print(el1, end=" ")
    print()