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
    
def Mux(x: int, y: int,sel: int):
    Nsel = Not(sel)
    a = And(x,Nsel)
    b = And(y,sel)
    return Or(a,b)

def Dmux(x: int, sel: int):
    Nsel = Not(sel)
    a = And(x,Nsel)
    b = And(x,sel)
    return a,b

def Not16(In: int, out: int):
    for i in range(len(In)):
        out[i] = Not(In[i])
    
    return out

def And16(In_A: int, In_B: int, out: int):
    for i in range(len(In_A)):
        out[i] = And(In_A[i],In_B[i])
    
    return out

def Or16(In_A: int, In_B: int, out: int):
    for i in range(len(In_A)):
        out[i] = Or(In_A[i],In_B[i])
    
    return out

def Mux16(In_A: int, In_B: int, sel: int, out: int):
    for i in range(len(In_A)):
        out[i] = Mux(In_A[i],In_B[i],sel)
    
    return out