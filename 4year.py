print("Ведите год: ")
a=int(input())
if a>1582:
    if a%4!=0:
        print("не високосный год")
        if a%100==0:
            if a%400==0:
                print("високосный год")
            else:
                print("не високосный год")
        else:
            print("високосный год")
    else:
        print("не високосный год")
else:
    print("error")
