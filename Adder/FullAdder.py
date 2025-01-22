import load
load.load()

import kairo

a = 0
b = 0
c = 0

w1 = kairo.And(a, b)
w2 = kairo.Xor(a, b)
w3 = kairo.And(w2, c)

sum = kairo.Xor(w2, c)
carry = kairo.Or(w1, w3)

print(carry,sum)