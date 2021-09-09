def last_dig(a,b,c):
    if (a*b)%10==c%10:
        return True
    else:
        return False
print("ведите a,b,c:")
a,b,c=map(int,input().split())
print(last_dig(a,b,c))
