#Наибольшая последовательнократная подпоследовательность
#https://www.e-olymp.com/ru/problems/264

def chain(p):
    res.append(p)
    k=p+1
    while k<len(A)-1:
        if A[res[-1]]%A[k]==0:
            chain(k)
        k+=1

res=[]
A=[100, 10,5,2,1]
chain(0)
print(res)