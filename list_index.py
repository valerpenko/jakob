s=[5,4,3,5,6,5,7,5]
k=0
while True:
    try:
        k=s.index(5,k)
        print(k)
        k += 1
    except ValueError:
        break

