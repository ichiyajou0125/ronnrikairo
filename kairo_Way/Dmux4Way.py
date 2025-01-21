import load
load.load()

import kairo

In = 1

sel = [0,0]

w1,w2 = kairo.Dmux(In,sel[0])
a,b = kairo.Dmux(w1,sel[1])
c,d = kairo.Dmux(w2,sel[1])

print(a,b,c,d)