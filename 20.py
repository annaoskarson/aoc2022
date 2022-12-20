data = [eval(a.strip()) for a in open('20.txt')]

def makelist(data, multi = 1):
    thelist = []
    for n, x in enumerate(data):
        thelist.append((n, x*multi))
    return(thelist)

def mix(thelist):
    i = 0
    while i < len(data):
        oldindex = [idx for idx, tup in enumerate(thelist) if tup[0] == i][0]
        item = thelist.pop(oldindex)
        newindex = oldindex + item[1]
        thelist.insert(newindex % (len(thelist)), item)
        i += 1
    return(thelist)

def zeroindex(thelist):
    return([idx for idx, tup in enumerate(thelist) if tup[1] == 0][0])


listorder = mix(makelist(data))
p1 = 0
for n in [1000, 2000, 3000]:
    _, num = listorder[(zeroindex(listorder) + n) % len(listorder)]
    p1 += num

print('1:', p1)


thekey = 811589153
listorder = makelist(data, thekey)
for _ in range(10):
    listorder = mix(listorder)

p2 = 0
for n in [1000, 2000, 3000]:
    _, num = listorder[(zeroindex(listorder) + n) % len(listorder)]
    p2 += num

print('2:', p2)
