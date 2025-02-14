import load
load.load()

import kairo

x = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
y = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]

zx = 0
nx = 0
zy = 0
ny = 0
f  = 0
no = 0

out = [0] * 16
zr = 0
ng = 0

out = [0] * 16
zr = 0
ng = 0

w1 = w2 = w3 = w4 = w5 = [0] * 16
AndXY = [0] * 16
AddXY = [0] * 16
Notw1 = Notw2 = Notw5 = [0] * 16

kairo.Mux16(x, [0] * 16, zx, w1)
kairo.Mux16(y, [0] * 16, zy, w2)

kairo.Not16(w1,Notw1)
kairo.Mux16(w1, Notw1, nx, w3)

kairo.Not16(w2,Notw2)
kairo.Mux16(w2, Notw2, ny, w4)

kairo.And16(w3, w4, AndXY)
AddXY = kairo.Add16(w3, w4)
kairo.Mux16(AndXY, AddXY, f, w5)

kairo.Not16(w5,Notw5)
kairo.Mux16(w5, Notw5, no, out)

out8bit = out[0:8]
out16bit = out[8:16]
ng = out[15]

or8bit = kairo.Or8Way(out8bit)
or16bit = kairo.Or8Way(out16bit)
outOr = kairo.Or(or8bit, or16bit)
zr = kairo.Not(outOr)