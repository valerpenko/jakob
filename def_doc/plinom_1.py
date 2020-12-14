p = ['0', '1', '2']
s = ""
k = 0


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


print(x(p))
