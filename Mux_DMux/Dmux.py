import load
load.load()

import kairo

a = 1

sel = 0

Nsel = kairo.Not(sel)

x = kairo.And(a,Nsel)
y = kairo.And(a,sel)

print("\nout1 :" +  str(x) + "\nout2 :" + str(y))