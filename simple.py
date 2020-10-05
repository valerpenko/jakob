startYear,stopYear=map(int,input().split())
months=[31,28,31,30,31,30,31,31,30,31,30,31]  #длинна месецов
res=[13]
for y in range(startYear,stopYear):
        for m in range(0,12):
            res.append(res[len(res)-1]+months[m])
            if m==1 and y%4==0:
                res[len(res) - 1]+=1
print(res)