# определить, "включен" ли 2-й бит в двоичном редставлении числа
a=2**10-1
print(a)
mask=4
if  a & mask > 0:
    print('on')
else:
    print('off')

# определить, сколько 1 в двоичном представлении числа
counter=0
mask=1
while mask<=2**31:
    if  a & mask > 0:
        counter+=1
    mask*=2
print(counter)

