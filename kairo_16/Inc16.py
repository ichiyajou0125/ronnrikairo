import load
load.load()

import kairo

a = [0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0]

out = [0] * 16

carry0, out[15] = kairo.FullAdder(a[15],1,0)
carry1, out[14] = kairo.FullAdder(a[14],0,carry0)
carry2, out[13] = kairo.FullAdder(a[13],0,carry1)
carry3, out[12] = kairo.FullAdder(a[12],0,carry2)
carry4, out[11] = kairo.FullAdder(a[11],0,carry3)
carry5, out[10] = kairo.FullAdder(a[10],0,carry4)
carry6, out[9] = kairo.FullAdder(a[9],0,carry5)
carry7, out[8] = kairo.FullAdder(a[8],0,carry6)
carry8, out[7] = kairo.FullAdder(a[7],0,carry7)
carry9, out[6] = kairo.FullAdder(a[6],0,carry8)
carry10, out[5] = kairo.FullAdder(a[5],0,carry9)
carry11, out[4] = kairo.FullAdder(a[4],0,carry10)
carry12, out[3] = kairo.FullAdder(a[3],0,carry11)
carry13, out[2] = kairo.FullAdder(a[2],0,carry12)
carry14, out[1] = kairo.FullAdder(a[1],0,carry13)
carry15, out[0] = kairo.FullAdder(a[0],0,carry14)

print(out)