def year(a):
 if a>1582:
    if a%4==0:
        if a%100==0:
            if a%400==0:
                year1=1
            else:
                year1 = 0
        else:
            year1 = 1
    else:
        year1 = 0
 else:
    year1 = 0
 return year1
def friday(day,yaer,b):
    codmauns=6
    codyaer=(6+yaer%100+year//100/4)%7

yer=2015
codyaer=(6+year%100+year%100/4)%7
print(codyaer)