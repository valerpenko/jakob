"""
Реализованны два варианта
"""
name=input("name: ")
s=input("ведите строку: ")
#Из стороки анб можнно составить имя анна
for c in name:
    if not(c in s):
        print("NO")
        exit()
print("yes")
#Из стороки анб нельзя составить имя анна
for c in name:
    if not (c in s):
        print("NO")
        exit()
    else:
        s=s.replace(c,"",1)
print("yes")