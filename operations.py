def AND(a,b):
    if a is True and b is True:
        return True
    elif a is True and b is False:
        return False
    elif a is False and b is True:
        return False
    elif a is False and b is False:
        return False

def OR(a,b):
    if a is True and b is True:
        return True
    elif a is True and b is False:
        return True
    elif a is False and b is True:
        return True
    elif a is False and b is False:
        return False

def XOR(a,b):
    if a is True and b is True:
        return False
    elif a is True and b is False:
        return True
    elif a is False and b is True:
        return True
    elif a is False and b is False:
        return False
