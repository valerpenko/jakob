n=int(input())
b=n
k=0
sym=0
while n > 0:
   n = n // 10
   k += 1
while b>9:
    right = a % 10
    left = a // (10 ** (k - 1))
    if right == left:
        sym+=1
    a = a % 10 ** (k - 1)
    a = a // 10
    k -= 2
if b>9:
    sym+=1
print(sum)