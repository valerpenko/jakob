print("ведите числа:")
l=list(map(int,input().split()))
if abs(min(l)-max(l))>10:
    l.sort()
    print(l)
else:
    print(l.pop())