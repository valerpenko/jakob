def x(p):
    x = ""
    b = ""
    s = ""
    for i in range(len(p)):
        b = p[i]
        if i > 0 and not i == 1:
            x = "x^" + str(i)
        elif i == 1:
            x = "x"
        if i == 0 and b != "0":
            s = p[i]
        elif b == "1":
            s = s + "+" + x
        elif b == "-1":
            s = s + "-" + x
        elif b[0] == "-":
            s = s + b + "*" + x
        elif b == "0":
            s = s
        elif not b == "0":
            s = s + "+" + b + "*" + x
    return s
# def polyMember(koef, index):
#     if koef==0:
#         return ""
#     res=""
#     if koef>0:
#         res+="+"
#     else:
#         res += "-"
#         koef=-koef
#     if index==0:
#         res+=str(koef)
#     else:
#         if koef==1:
#             pass
#         else:
#             res+=str(koef)
#     if index==0:
#         pass
#     elif index==1:
#         res += "*x"
#     else:
#         res += "*x^"+str(index)
#     return res

def polyMember(koef, index):
    if koef==0:
        return ""
    res=""
    if koef>0:
        res+="+"
    else:
        res += "-"
        koef=-koef
    if index==0:
        return res+str(koef)
    elif index==1:
        if koef==1:
            return res+"x"
        else:
            return res+str(koef)+"*x"
    else:
        if koef==1:
            return res + "x^"+str(index)
        else:
            return res + str(koef) + "*x^"+str(index)


def showPolynom(koefs):
    res=""
    for i in range(len(koefs)):
        res+=polyMember(koefs[i], i)
    if res[0]=="+":
        res = res[1:]
    # if res[0]=="*":
    #     res=res[1:]
    return res


p = [0, -3, 0, 1, -2]
#s = ""
#k = 0
#print(x(p))

print(showPolynom(p))


