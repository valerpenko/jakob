a=223
b=0
k=0
while a>0:
    k=a%10
    b=b*10+k
    #print(k,end=':')
    a=a//10
print(b)


a=223
a=str(a)
b=list(a)
# b=b.reverse()
b.reverse()
c = ''.join(b)
c=int(c)
print(c)

   
