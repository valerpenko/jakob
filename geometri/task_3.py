from kosenkov_1 import distance
points=[[10,3],[7,6],[-2,5],[2,0],[10,-4]]
for k in range(0,len(points)) :
    if k==len(points)-1:
        min = distance(points[k], points[0])
        min_poz = 0
    else:
        min = distance(points[k], points[k+1])
        min_poz = k+1
    for i in range(0,len(points)):
        if i!=k:
            d=distance(points[k],points[i])
            if min>d:
                min_poz=i
                min=d
    print(min_poz)