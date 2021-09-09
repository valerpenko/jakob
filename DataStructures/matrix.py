import random
n=6
l=[]
for i in range(n):
    l_n = []
    for i_n in range(n):
        l_n.append(random.randint(1,10))
    l.append(l_n)
print(l)

