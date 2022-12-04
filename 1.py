# nu kör vi!
import os

print("1:1")
#print(os.listdir())   

with open("1.txt","r") as f:
    cal = f.read()
    
#print(cal)

cal = cal.split("\n")
m = 0
s = 0
l = []
for c in cal[:-1]:
    c = c.strip()
    #print(c, int(c))
    if len(c) == 0:
        m = max (m, s)
        l.append(s)
        s = 0
    else:
        #print("@", c)
        #print("$"+c+"&")
        s += int(c)
    #print(c, s, m)
#print(m)
l.sort()
#print(l)
top = l[-3:]
#print(top)

print(m)
print("1:2")
print(sum(top))
#print(sum(l[-3:]))
