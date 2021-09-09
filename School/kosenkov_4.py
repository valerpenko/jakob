L=list(input().split())
str=' '.join(L)
if str.find("привет")!=-1:
    print("привет "*10)
else:
    print(L.pop())
