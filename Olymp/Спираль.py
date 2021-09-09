n=int(input())
l=[[0 for i in range(n)] for i in range(n)]
dir='right'
x=0
y=0
l[x][y]=1
r_1=True
l_1=True
d_1=True
while True:
    if dir=="right":
        if x<n and l[y][x+2]==0:
            x+=1
            l[y][x] = 1
        else:
            dir="down"
    if dir=="down":
        if y<n and l[y+2][x]==0:
            y+=1
            l[y][x] = 1
        else:
            dir="left"
    if dir=="left":
        if x>0 and l[y][x-2]==0:
            x-=1
            l[y][x] = 1
        else:
            dir="up"
    if dir=="up":
        if l[y-2][x]==0:
            y-=1
            l[y][x] = 1
        else:
            if l[y+2][x]==1:
                dir="right"
            else:
                break