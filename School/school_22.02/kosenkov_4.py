def is_perfect(n):
    sum = 0
    for i in range(1, int(n/2)+1):
        if n % i == 0:
            sum += i
        print(i)
    print("Сумма",sum)
    return sum == n

is_perfect(int(input()))
