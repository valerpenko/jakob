def firstFriday(startYear):    #первая пятница
    k=2
    for i in range(1921,startYear+1):
        if (i-1)%4==0:
            k=k-2
            if k<=0:
                k=k+7
        else:
            k=k-1
            if k<=0:
                k=k+7
    return k

def get13s(startYear, stopYear):             #число 13
    months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30]  # длинна месецов
    res = [13]
    for y in range(startYear, stopYear + 1):
        for m in range(0, 11):
            res.append(res[len(res) - 1] + months[m])
            if m == 1 and y % 4 == 0:
                res[len(res) - 1] += 1
    return res
def freeFridays(startYear, stopYear):
    _13s=get13s(startYear, stopYear)
    fridays=0
    for el in _13s:
        if el%7 == firstFriday(startYear):
            fridays+=1
    return fridays

k=int(input())
days=0
for i in range(0,k):
    a,b=map(int,input().split())
    days+=freeFridays(a,b)
print(days)
