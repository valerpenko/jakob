def Hanoi(q,frome,to,buf):
    if q==0:
        return
    else:
        Hanoi(q-1,frome,buf,to)
        print('диск размером ',q," перенесен с ",frome," на ",to)
        Hanoi(q-1,buf,to,frome)
def move(q,x,y):
    if x +y==3:
        buf=3
    elif x+y==4:
        buf=2
    elif x+y==5:
        buf=1
    if q==0:
        return
    else:
        move(q-1,x,buf)
        print('диск размером ',q," перенесен с ",x," на ",y)
        move(q-1,buf,y)
#Hanoi(3,1,3,2)
x=1
y=3
buf=2
move(3,x,y)