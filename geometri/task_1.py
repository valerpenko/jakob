from kosenkov_1 import intersection_point,line_equation,contains
#l1,l2 - концы отрезков
l1=[2,4]
l2=[3,5]
#t1,t2,t3- вершины треугольника
t1=[2,4]
t2=[5,6]
t3=[3,8]
l1l2=line_equation(l1,l2)
t1t2=line_equation(t1,t2)
t2t3=line_equation(t2,t3)
t3t1=line_equation(t3,t1)
k=0
p12=intersection_point(l1l2,t1t2)
p23=intersection_point(l1l2,t2t3)
p31=intersection_point(l1l2,t3t1)
if contains(t1,t2,p12)==1:
    k+=1
if contains(t2,t3,p23)==1:
    k+=1
if contains(t3,t1,p31)==1:
    k+=1
if k == 0 :
    print("отрезок не пересикает треуголльник")
if k ==1:
    print("отрезок входит в треугольник")
if  k==2:
    print("отрезок пресекает треугольник")