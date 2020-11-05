import math
def s_ches(a,b,z):
    t_a=a*(2**0.5)
    l=b/math.sin(z)
    t_b=(2**0.5)*(a-l*math.cos(z))
    h=((b**2)*((t_a-t_b)**2)/4)**0.5
    s=(a+b)/2*math.sqrt((c**2))
    return s
a,b,z=map(float,input().split())
print(s_ches(a,b,z))

