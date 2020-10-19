
n=54845

a=n
b=a
print(a)
# k - количество цифр числа
k=0
while b >0:
    b=b//10
    k+=1

#проверка симметричности
sym=True
while a>9:
  right=a%10
  left=a//(10**(k-1))
  if right!=left:
      sym=False
      break
  # отбрасываем крайние цифры от числа
  a=a%10**(k-1)
  a=a//10
  k-=2
print(sym)

s=str(n)
k=len(s)
sym=True
for i in range(k//2):
    if s[i] != s[-1-i]:
       sym=False
       break
print(sym)


