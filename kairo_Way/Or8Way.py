import load
load.load()

import kairo

In = [0,0,0,0,0,0,0,0]

a = kairo.Or(In[0],In[1])
b = kairo.Or(In[2],In[3])
c = kairo.Or(In[4],In[5])
d = kairo.Or(In[6],In[7])

e = kairo.Or(a,b)
f = kairo.Or(c,d)

out = kairo.Or(e,f)

print(out)