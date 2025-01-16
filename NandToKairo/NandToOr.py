import load
load.load()

import kairo

a = 1
b = 1

x = kairo.Nand(a,a)
y = kairo.Nand(b,b)

out = kairo.Nand(x,y)

print(out)