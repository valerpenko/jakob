def rect_area(r):
    return (r[2]-r[0])*(r[3]-r[1])
def rect_intersection(r1,r2):
    hor1=[r1[2],r1[0]]
    hor2=[r2[2],r2[0]]
    ver1=[r1[3],r1[1]]
    ver2=[r2[3],r2[1]]
    hor=line_intersection(hor1,hor2)
    ver = line_intersection(ver1, ver2)
    return hor[0],ver[0],hor[1],ver[1]

def line_intersection(line1,line2):
    if line1[0]>line2[0]:
        line1[0],line1[1]=line2[0],line2[1]
    if line1[0]<line2[0]<line1[1]<line2[1]:
        return line2[0],line1[1]
    else:
        return 0,0
rectangles=[[1,5,4,7],[2,2,5,6],[3,5,8,8]]
while len(rectangles)!=1:
    rect=rect_intersection(rectangles[0],rectangles[1])
    if rect_area(rect)==0:
        print("нет общего пересечения")
        exit()
    rectangles.pop(0)
    rectangles.pop(0)
    rectangles.insert(0,rect)
print(rect_area(rect))