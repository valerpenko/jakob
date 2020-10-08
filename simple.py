startYear,stopYear=map(int,input().split())
months=[31,28,31,30,31,30,31,31,30,31,30]  #длинна месецов
res=[13]
for y in range(startYear,stopYear+1):
        for m in range(0,11):
            res.append(res[len(res)-1]+months[m])
            if m==1 and y%4==0:
                res[len(res) - 1]+=1
print(res)