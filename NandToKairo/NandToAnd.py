import load
load.load()

import kairo

a = 1
b = 1

x = kairo.Nand(a,b)
y = kairo.Nand(a,b)

out = kairo.Nand(x,y)

print(out)