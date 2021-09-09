def faktor(n):
    sqrt=n**0.5
    for i in range(int(sqrt)):
        p = int(sqrt) + 1
        q = int(sqrt) - i
        for h in range(i):
            if (p+h)*q==n:
                return q, (p+h)
        p = int(sqrt) + i+1
        q = int(sqrt)
        for v in range(i):
            if p*(q-h)==n:
                return q-h, p

        if int(sqrt+i+1)*int(sqrt-i)==n:
            return int(sqrt+i+1), int(sqrt-i)
print(faktor(99873791))