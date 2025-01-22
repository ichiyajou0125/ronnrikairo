import load
load.load()

import kairo

a = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
b = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

out = [0] * 16

carry0, out[15] = kairo.FullAdder(a[15],b[15],0)
carry1, out[14] = kairo.FullAdder(a[14],b[14],carry0)
carry2, out[13] = kairo.FullAdder(a[13],b[13],carry1)
carry3, out[12] = kairo.FullAdder(a[12],b[12],carry2)
carry4, out[11] = kairo.FullAdder(a[11],b[11],carry3)
carry5, out[10] = kairo.FullAdder(a[10],b[10],carry4)
carry6, out[9] = kairo.FullAdder(a[9],b[9],carry5)
carry7, out[8] = kairo.FullAdder(a[8],b[8],carry6)
carry8, out[7] = kairo.FullAdder(a[7],b[7],carry7)
carry9, out[6] = kairo.FullAdder(a[6],b[6],carry8)
carry10, out[5] = kairo.FullAdder(a[5],b[5],carry9)
carry11, out[4] = kairo.FullAdder(a[4],b[4],carry10)
carry12, out[3] = kairo.FullAdder(a[3],b[3],carry11)
carry13, out[2] = kairo.FullAdder(a[2],b[2],carry12)
carry14, out[1] = kairo.FullAdder(a[1],b[1],carry13)
carry15, out[0] = kairo.FullAdder(a[0],b[0],carry14)

print(out)