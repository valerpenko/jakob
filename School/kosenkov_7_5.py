n=int(input())
divider=10
sum=0
digits=1
for k in range(1,n+1):
    if k%divider==0:
        divider*=10
        digits += 1
    sum+=digits/k**2
print(sum)