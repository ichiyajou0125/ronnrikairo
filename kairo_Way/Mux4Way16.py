import load
load.load()

import kairo

In_A = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
In_B = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
In_C = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
In_D = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

sel = [0,0]

out_X = [0] * 16
out_Y = [0] * 16
output = [0] * 16

out_X = kairo.Mux16(In_A,In_B,sel[1],out_X)
out_Y = kairo.Mux16(In_C,In_D,sel[1],out_Y)
output = kairo.Mux16(out_X,out_Y,sel[0],output)

print(output)