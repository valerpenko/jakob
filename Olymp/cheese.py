import math
def trap_cheese(a,b,z):
    t_a=a*math.sqrt(2)
    l=b/math.sin(z)
    t_b=math.sqrt(2)*(a-l*math.cos(z))
    h=((b**2)*math.sqrt((t_a-t_b)**2)/4)
    s=
    return s
def tria_cheese(a,b,z):
    t_a=a*math.sqrt(2)

a,b,z=map(float,input().split())
print(trap_cheese(a,b,z))

