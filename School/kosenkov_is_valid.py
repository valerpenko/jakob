def is_valid(a):
    if len(a)>=4 and len(a)<=6:
        try:
            if type(int(a))==int:
                return True
        except(ValueError):
                return False
    else:
        return False
