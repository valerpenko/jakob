import math
def math_for_rest(k,a):
    if a<=k:
        return 3+(a-1)*2
    else:
        return 6+(a-2)*2
n=int(input())
# n=int(input())
# k=math.floor(n**0.5)#размер большого квадрата
# match_for_right_square=2 * k * (k + 1)
# full =match_for_right_square+math_for_rest(k,n - k ** 2)
# print(full)
k=math.floor(n**0.5)
if k**2<n<(k+1)**2:
    a=n-k**2
    full=math_for_rest(k,a)+2*k*(k+1)
    print(full)
else:
 print(2*k*(k+1))
