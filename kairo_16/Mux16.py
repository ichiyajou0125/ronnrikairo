import load
load.load()

import kairo

In_A = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
In_B = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
sel = 0
Out = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

Out[0] = kairo.Mux(In_A[0],In_B[0],sel)
Out[1] = kairo.Mux(In_A[1],In_B[1],sel)
Out[2] = kairo.Mux(In_A[2],In_B[2],sel)
Out[3] = kairo.Mux(In_A[3],In_B[3],sel)
Out[4] = kairo.Mux(In_A[4],In_B[4],sel)
Out[5] = kairo.Mux(In_A[5],In_B[5],sel)
Out[6] = kairo.Mux(In_A[6],In_B[6],sel)
Out[7] = kairo.Mux(In_A[7],In_B[7],sel)
Out[8] = kairo.Mux(In_A[8],In_B[8],sel)
Out[9] = kairo.Mux(In_A[9],In_B[9],sel)
Out[10] = kairo.Mux(In_A[10],In_B[10],sel)
Out[11] = kairo.Mux(In_A[11],In_B[11],sel)
Out[12] = kairo.Mux(In_A[12],In_B[12],sel)
Out[13] = kairo.Mux(In_A[13],In_B[13],sel)
Out[14] = kairo.Mux(In_A[14],In_B[14],sel)
Out[15] = kairo.Mux(In_A[15],In_B[15],sel)

print(Out)