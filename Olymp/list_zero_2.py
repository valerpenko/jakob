import random
list=[]
N=5
arr=[i+1 for i in range(N)]
while len(arr)>0:
    r_k=random.randint(0,len(arr)-1)
    r_v=arr.pop(r_k)
    list.append(r_v)
print(list)
i=random.randint(0,len(list)-1)
list[i]=0
i2=random.randint(0,len(list)-1)
while i2==i:
    i2 = random.randint(0, len(list) - 1)
list[i2]=0
print(list)
arr=[i+1 for i in range(N)]
for el in list:
    if el != 0 :
        arr.remove(el)
print(arr)
