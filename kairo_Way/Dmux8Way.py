import load
load.load()

import kairo

In = 1

sel = [0,0,0]

v1,v2 = kairo.Dmux(In,sel[0])

w1,w2 = kairo.Dmux(v1,sel[1])
w3,w4 = kairo.Dmux(v2,sel[1])

a,b = kairo.Dmux(w1,sel[2])
c,d = kairo.Dmux(w2,sel[2])
e,f = kairo.Dmux(w3,sel[2])
g,h = kairo.Dmux(w4,sel[2])

print(a,b,c,d,e,f,g,h)