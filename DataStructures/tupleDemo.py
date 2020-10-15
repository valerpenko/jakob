a=(3,4,5)
b=(4,True, 'ww')
print (len(a))
print (len(b))

print (a[0])
print (b[1])

for i in range(0,len(a)):
    print(a[i])
print("===")
for el in a:
    print(el)
print("===")
for i in range(len(a)):
    print(a[len(a)-i-1])
print("===")
#for i in range(len(a),1,-1):   как???
#    print(a[i])
b[1]="OK"
print(b)
print(a+a)