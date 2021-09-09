def sum_upp(x):
    if x < 10:
        return x
    else:
        return x%10+sum_upp(x//10)

a=int(input())
print(sum_upp(a))