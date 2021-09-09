def acerman(m,n):
    if m==0:
        if len(s[0])>n:
            return s[m][n]
        else:
            k =len(s[0])
            while k <=n:
                s[0].append(k+1)
                k+=1
            return n+1

    else:
        if  n==0:
            return acerman(m-1,1)
        else:
            a=acerman(m,n-1)
            return acerman(m-1,a)

m,n=map(int,input().split())
s=[[1],[],[],[]]
print(acerman(m,n))
