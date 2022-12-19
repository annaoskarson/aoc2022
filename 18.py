R = set([tuple([int(x) for x in a.strip().split(',')]) for a in open('18.txt')])

def nbs(point, R): # The neighbours NOT made of stone
    N = set()
    x,y,z = point
    N.update([(x1,y,z) for x1 in [x-1, x+1] if (x1,y,z) not in R])
    N.update([(x,y1,z) for y1 in [y-1, y+1] if (x,y1,z) not in R])
    N.update([(x,y,z1) for z1 in [z-1, z+1] if (x,y,z1) not in R])
    return(N)

total = sum(len(nbs(cube, R)) for cube in R)

xmin, xmax = min(R, key = lambda t: t[0])[0], max(R, key = lambda t: t[0])[0]
ymin, ymax = min(R, key = lambda t: t[1])[1], max(R, key = lambda t: t[1])[1]
zmin, zmax = min(R, key = lambda t: t[2])[2], max(R, key = lambda t: t[2])[2]

basin = [(xmin-1, ymin-1, zmin-1), (xmax+1, ymax+1, zmax+1)]

def inbasin(point):
    x1, y1, z1 = point
    return(basin[0][0] <= x1 <= basin[1][0] and basin[0][1] <= y1 <= basin[1][1] and basin[0][2] <= z1 <= basin[1][2])

W = set() # Already seen
Q = [(xmin-1, ymin-1, zmin-1)] 
maxQ = 0
p2 = 0
while Q:
    this = Q.pop(0)
    if this not in W:
        W.add(this)
        ns = nbs(this, R) # Neigbours not made of stone
        p2 += 6-len(ns) # Number of surfaces with rock
        Q.extend([n for n in ns if inbasin(n)]) # Important to not look outside the basin!

print('1:', total)
print('2:', p2)