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
    for i in range(len(l)-1):
        if int(l[i][-1])-int(l[i+1][-1])==1:
            continue
        elif
        else:
            l.insert(i+1,"+0*x^"+str(int(l[i][-1])-1))

    #преобрвзовываем ствроки одночлены в список коэфицентов
    for i in range(len(l)):
        l[i]=int(l[i][:l[i].find("*")])
    return l

def calculate(poly,x):
    sum=0
    poly=poly[::-1]
    for i in range(len(poly)):
        sum+=poly[i]*x**i
    return sum

l=""input()""
x=int(input())
poly=string_to_list(l)
print(poly)
print(calculate(poly,x))

