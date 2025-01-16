import load
load.load()

import kairo

a = 1
b = 1

c = kairo.Nand(a,b)
x = kairo.Nand(a,c)
y = kairo.Nand(b,c)

out = kairo.Nand(x,y)

print(out)