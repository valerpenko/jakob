def myUpper(s):
   s1=''
   #for i in range(0, len(s)):
   for c in s:
      if  c.islower():
         s1+=chr(ord(c)-32)
      else:
         s1+=c
   return s1

print(myUpper("AbCdEf"))
print(myUpper(input()))
