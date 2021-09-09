k = 0
a = int(input())
max = a
while a != 0:
    if a > max:
        max = a
        k = 1
    elif a == max:
        k += 1
    a= int(input())
print(k)

