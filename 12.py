themap = [list(a.strip()) for a in open('12.txt')]

def nbs(coord):
    x,y = coord
    nblist = []
    for y1 in [y-1, y+1]:
        if y1 > len(themap)-1 or y1 < 0:
            continue
        if ord(themap[y1][x]) <= ord(themap[y][x]) + 1:
            nblist.append((x, y1))
    for x1 in [x-1, x+1]:
        if x1 > len(themap[0])-1 or x1 < 0:
            continue
        if ord(themap[y][x1]) <= ord(themap[y][x]) + 1:
            nblist.append((x1, y))
    return(nblist)

for y,row in enumerate(themap):
    for x, c in enumerate(row):
        if c == 'S':
            S = (x,y)
            themap[y][x] = 'a'
        if c == 'E':
            E = (x,y)
            themap[y][x] = 'z'

def path(S, E):
    Q = [(S, 0)]
    V = set()
    while len(Q) > 0:
        coord, l = Q.pop(0)
        if coord in V: # But why is this needed? Hm.
            continue
        V.add(coord)
        if coord == E:
            return(l) # DONE
        else:
            nb = nbs(coord)
            for n in nb:
                if n not in V:
                    Q.append((n, l+1))
    return(9999) # NO SOLUTION

shortest = 999
for y,row in enumerate(themap):
    for x,c in enumerate(row):
        if c == 'a':
            shortest = min(shortest, path((x,y), E))

print('1:', path(S, E))
print('2:', shortest)