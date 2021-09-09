def three_letter_collection(s):
    l=[]
    while len(s)>=3:    #находимся в цыкле пока длина строки > или = 3
        l.append(s[:3])
        s=s[1:]
    return sorted(l)
s=input("ведите строку: ")# ввод служит для проверки функции
print(three_letter_collection(s))