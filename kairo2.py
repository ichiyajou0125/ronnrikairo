def Not(x: int) -> int:
    if(x == 1):
        return 0
    else:
        return 1

def Or(x: int, y: int):
    if(x == 1):
        return 1
    elif(y == 1):
        return 1
    else:
        return 0

def And(x: int, y: int):
    if(x == 1):
        if(y == 1):
            return 1
        else:
            return 0
    else:
        return 0
    
def Nor(x: int, y: int):
    if(x == 1):
        return 0
    elif(y == 1):
        return 0
    else:
        return 1
    
def Nand(x: int, y: int):
    if(x == 1):
        if(y == 1):
            return 0
        else:
            return 1
    else:
        return 1

def Xor(x: int, y: int):
    if(x == y):
        return 0
    else:
        return 1
    
def Xnor(x: int, y: int):
    if(x == y):
        return 1
    else:
        return 0