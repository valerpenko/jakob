a=64
#s=''
s=[]
if a>0:
 while a!=0:
    #s.append(a%2)
    s.insert(0,a%2)
    a=a//2
 s.insert(0,0)
 print(s)
else:
 a=abs(a)
 while a!=0:
    #s.append(a%2)
    s.insert(0,a%2)
    a=a//2
 s.insert(0,0)

 for i in range(len(s)):
    if s[i]==0:
        s[i]=1
    else:
        s[i]=0


#for i in range(-1,-len(s)-1,-1):
 i=len(s)-1
 while s[i]==1:
    s[i]=0
    i=i-1
 s[i]=1

 print(s)