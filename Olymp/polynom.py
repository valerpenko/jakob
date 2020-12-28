def string_to_list(s):
    #разбеваем строку много член на список строк одночелнов
    if s[0]!="-":
        s="+"+s
    l=[]
    i=0

    while True:
        i_plus=s.find("+",1)
        i_minus=s.find("-",1)
        if i_plus<i_minus and i_plus>=0:
            i=i_plus
        elif i_minus<i_plus and i_minus>=0:
            i=i_minus
        elif i_plus==-1:
            i=i_minus
        elif i_minus==-1:
            i=i_plus
        if i == -1 :
            l.append(s)
            break
        l.append(s[:i])
        s=s[i:]
    #явно добовляем показатели степени х
    for i in range(len(l)):
        if l[i][-1]=="x":
            l[i]=l[i]+"^1"
        if l[i].find("x")==-1:
            l[i] = l[i] + "*x^0"
    #преобрвзовываем ствроки одночлены в список коэфицентов
    k=s.find("^")
    pow=s[k:]
    pow=int(pow)
    list=[l]




    return l
def calculate(poly,x):
    sum=0
    poly=poly[::-1]
    for i in range(len(poly)):
        sum+=poly[i]*x**i
    return sum
s="8*x^4-5*x^2+7*x-6"

print(string_to_list(s))


