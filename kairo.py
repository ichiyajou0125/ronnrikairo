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

def Or8Way(In: int):
    a = Or(In[0],In[1])
    b = Or(In[2],In[3])
    c = Or(In[4],In[5])
    d = Or(In[6],In[7])

    e = Or(a,b)
    f = Or(c,d)

    out = Or(e,f)
    return out

def Mux4Way16(In_A: int, In_B: int, In_C: int, In_D: int, sel: int):
    out_X = [0] * 16
    out_Y = [0] * 16
    out = [0] * 16

    out_X = Mux16(In_A,In_B,sel[1],out_X)
    out_Y = Mux16(In_C,In_D,sel[1],out_Y)
    out = Mux16(out_X,out_Y,sel[0],out)
    return out

def Mux8Way16(In_A: int, In_B: int, In_C: int, In_D: int, In_E: int, In_F: int, In_G: int, In_H: int, sel: int):
    out_V = [0] * 16
    out_W = [0] * 16
    out_X = [0] * 16
    out_Y = [0] * 16
    w1 = [0] * 16
    w2 = [0] * 16
    out = [0] * 16

    out_V = Mux16(In_A,In_B,sel[2],out_V)
    out_W = Mux16(In_C,In_D,sel[2],out_W)
    w1 = Mux16(out_V,out_W,sel[1],w1)

    out_X = Mux16(In_E,In_F,sel[2],out_X)
    out_Y = Mux16(In_G,In_H,sel[2],out_Y)
    w2 = Mux16(out_X,out_Y,sel[1],w2)

    out = Mux16(w1,w2,sel[0],out)
    return out

def HarfAdder(In_A: int, In_B: int):
    sum = Xor(In_A,In_B)
    carry = And(In_A,In_B)

    return carry,sum

def FullAdder(In_A: int, In_B: int, In_C: int):
    w1 = And(In_A,In_B)
    w2 = Xor(In_A,In_B)
    w3 = And(w2, In_C)

    sum = Xor(w2, In_C)
    carry = Or(w1, w3)

    return carry,sum

def Add16(In_A: int, In_B: int):
    out = [0] * 16
    carry = 0

    for i in range(16):
        Index = 15-i
        carry, out[Index] = FullAdder(In_A[Index],In_B[Index],carry)

    return out

def Inc16(In: int):
    out = [0] * 16
    carry = 0

    carry0, out[15] = FullAdder(In[15],1,0)
    for i in range(1,16):
        Index = 15-i
        carry, out[Index] = FullAdder(In[Index],0,carry)

    return out