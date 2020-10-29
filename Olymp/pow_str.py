str=input()
a=str[0]
poz=len(a)
while poz<len(str) and str[poz:len(a)]==a :
    poz += len(a)
if poz>=len(str):
    print("")
else:
    a=a+