import load
load.load()

import kairo

a = 1
b = 0
sel = 1

Nsel = kairo.Not(sel)

x = kairo.And(a,Nsel)
y = kairo.And(b,sel)
out = kairo.Or(x,y)
print(out)