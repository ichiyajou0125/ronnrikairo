import load
load.load()

import kairo

a = 0
b = 0

sum = kairo.Xor(a,b)
carry = kairo.And(a,b)

print(carry,sum)