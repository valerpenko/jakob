def check_string_decomposition(str,part):
    pos=0
    k=0
    while pos<len(str):
        if str[pos:pos+len(part)] == part:
            pos+=len(part)
            k+=1
        else:
            return 0
    return k




str=input()
part=str[0]
check=check_string_decomposition(str,part)
while check==0:
    part = part + str[len(part)]
    check = check_string_decomposition(str, part)
print(check)
print(part)




















# part=str[0]
# len_part=len(part)
# while len_part<len(str) and str[len_part:len(part)]==part :
#     len_part += len(part)
# if len_part>=len(str):
#     print("")
# else:
#