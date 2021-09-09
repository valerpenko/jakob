n=int(input("введите n:"))
k=False
for i in range(n):
    l=int(input())
    if -100<l<=-10:
        i_f=l
        i_k=i
        k=True
if k==True:
    print(i_f,"номер:",i_k)
else:
    print("NO")

# nums = [int(el) for el in input().split()]
#
# answer = [el for el in nums if -100<=el<-10]
# try:
#     print(answer[-1])
# except:
#     print("no")
