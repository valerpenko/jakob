l1=[1,3,5,8,10]
l2=[2,6,9,11,15]
l=[]

while len(l1)>0 and len(l2)>0:
    if l1[0]<l2[0]:
        l.append(l1.pop(0))
    else:
        l.append(l2.pop(0))
if len(l1)==0:
    l=l+l2
else:
    l=l+l1
print(l)