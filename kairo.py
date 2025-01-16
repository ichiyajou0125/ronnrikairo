def Not(x: int) -> int:
    return 0 if x else 1

def Or(x: int, y: int):
    if(x or y == 1):
        return 1
    else:
        return 0

def And(x: int, y: int):
    if(x and y == 1):
        return 1
    else:
        return 0
    
def Nor(x: int, y: int):
    if(x or y == 1):
        return 0
    else:
        return 1
    
def Nand(x: int, y: int):
    if(x and y == 1):
        return 0
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
    
