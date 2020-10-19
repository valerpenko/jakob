# определить, "включен" ли 2-й бит в двоичном редставлении числа

a=2**61-1

print(a)
mask=4
counter1=0
counter=0
mask=1
mask1=1
while mask1<=2**64:
    if  a & mask1 == 0:
        counter1+=1
    mask1*=2
while mask<=2**64:
    if  a & mask > 0:
        counter+=1
    mask*=2
#print("В числе ",a, " ", counter1, "нулей и ", counter, "единиц.")

print("В числе %20d  %2d нулей и %2d единиц" % (a, counter1, counter))