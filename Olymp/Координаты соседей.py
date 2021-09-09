m,n=map(int,input().split())
x,y=map(int,input().split())
"""#Точки в углах
if x==1 and y==1:
    print(1, 2)
    print(2, 1 )
if x==m and y==1:
    print(m-1,1)
    print(m,2)



#Точки по краям
if y==1 and 1<x<m :
    print(x-1,1)
    print(x+1,1)
    print(x,2)"""
l=[[x-1,y],[x,y-1],[x+1,y],[x,y+1]]
for el in l:
    if 0<el[0]<=m and 0<el[1]<=n:
        print(el[0],el[1])


