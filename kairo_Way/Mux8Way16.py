import load
load.load()

import kairo

In_A = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
In_B = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
In_C = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
In_D = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
In_E = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
In_F = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
In_G = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
In_H = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

sel = [0,0,0]

out_V = [0] * 16
out_W = [0] * 16
out_X = [0] * 16
out_Y = [0] * 16
w1 = [0] * 16
w2 = [0] * 16
output = [0] * 16

out_V = kairo.Mux16(In_A,In_B,sel[2],out_V)
out_W = kairo.Mux16(In_C,In_D,sel[2],out_W)
w1 = kairo.Mux16(out_V,out_W,sel[1],w1)

out_X = kairo.Mux16(In_E,In_F,sel[2],out_X)
out_Y = kairo.Mux16(In_G,In_H,sel[2],out_Y)
w2 = kairo.Mux16(out_X,out_Y,sel[1],w2)

output = kairo.Mux16(w1,w2,sel[0],output)
print(output)