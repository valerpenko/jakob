def summ(poly1,poly2):
    poly1=poly1[::-1]
    poly2=poly2[::-1]
    poly_new=[]
    while len(poly1)>0 and len(poly2)>0:
        poly_new.append(poly1[0]+poly2[0])
        poly1.pop(0)
        poly2.pop(0)
    if len(poly1)==0:
        poly_new.extend(poly2)
    else:
        poly_new.extend(poly1)
    poly_new=poly_new[::-1]
    return poly_new

def get_part(s):
    plus = s.find("+", 1)
    minus = s.find("-", 1)
    if plus == -1:
        plus=len(s)+1
    if minus == -1:
        minus=len(s)+1
    pos=min(plus,minus,len(s))
    s_smoll=s[:pos]
    s=s[pos: ]
    star=s_smoll.find("*")
    if star>=0:
        k=s_smoll[:star]
    else:
        k=s_smoll
    k=int(k)
    cap=s_smoll.find("^")
    if cap != -1 :
        p=int(s_smoll[cap+1:])
    elif s_smoll.find("x")!=-1:
        p=1
    else:
        p=0
    return s,k,p
def calculate(poly,x):
    sum = 0
    poly = poly[::-1]
    for i in range(len(poly)):
        sum += poly[i] * x ** i
    return sum
def string_2_poly(s):
    s, k, p = get_part(s)
    koeffs = [0] * (p + 1)
    koeffs[0] = k
    while len(s) > 0:
        s, k, p = get_part(s)
        koeffs[len(koeffs) - 1 - p] = k
    return koeffs
s=input()
s1=input()
x=int(input())

print(summ(string_2_poly(s),string_2_poly(s1)))
