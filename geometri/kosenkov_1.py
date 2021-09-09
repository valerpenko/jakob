#1
def line_equation(v,w):
    a=v[1]-w[1]
    b=w[0]-v[0]
    c=(w[1]-v[1])*v[0]+(v[0]-w[0])*v[1]
    return a,b,c
#n
def distance(p1,p2):
    return ((p1[0]-p2[0])**2+(p1[1]-p2[1])**2)**0.5
#2
def intersection_point(line1,line2):
    if line1[0]*line2[1]==line2[0]*line1[1]:
        return False
    else:
        x=-(line1[2]*line2[1]-line2[2]*line1[1])/(line1[0]*line2[1]-line2[0]*line1[1])
        y=(line2[1]*line1[2]-line1[0]*line2[2])/(line1[0]*line2[1]-line2[0]*line1[1])
        return x,y
# Принадлежность некоторой точки отрезку V x ;V y )-W x ;W y ):
# Координаты точек отрезка можно задать двумя параметрическими уравнениями от одной
# независимой переменной t:
# x=V x +(W x -V x )*t,t=(x-Vx)/(W x -V x )
# y=V x +(W y -V y )*t.
# При 0<=t<=1 точка x, y) лежит на отрезке, а при t<0 или t>1 — вне отрезка на прямой линии,
# n
def contains(p1,p2,p):
    tx=(p[0]-p1[0])/(p2[0]-p1[0])
    ty = (p[1] - p1[0]) / (p2[0] - p1[0])
    if tx!=ty:
        return -1   #не лежит на прямой
    elif 0<=tx<=1:
        return 1    #лежит в отрезке
    else:
        return 0    #лежит на продолжении отрезка 