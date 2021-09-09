def palindromic_date(s):
    s1=s[0:2]+s[3:5]+s[6:]
    s2=s[3:5]+s[0:2]+s[6:]
    if s1==s1[::-1] and s2==s2[::-1]:
        return True
    else:
        return False

