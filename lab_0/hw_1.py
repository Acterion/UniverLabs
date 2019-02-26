
# coding: utf-8

# In[10]:


import re
l=[]
ls=[]
s=set()
with open('input.txt') as f:
    text = f.read()
l=re.findall(r'\d+', text)
for e in l:
    e=int(e)
    ls.append(e)
    s.add(e)
    ls.sort()
    if s.symmetric_difference(range(ls[0],ls[len(ls)-1]+1)) == set() or len(s)==1:
        print("Packet %s-%s is complete"%(ls[0],ls[len(ls)-1]))
    else:
        print("These elements aren`t in list:")
        print(s.symmetric_difference(range(ls[0],ls[len(ls)-1]+1)))

