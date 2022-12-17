data = [a.strip() for a in open('14.txt')]

themap = set()

def draw(m, fr, to):
    x1, y1 = int(fr.split(',')[0]), int(fr.split(',')[1])
    x2, y2 = int(to.split(',')[0]), int(to.split(',')[1])
    for i in range(min(y1, y2), max(y1, y2) + 1):
        for j in range(min(x1, x2), max(x1, x2) + 1):
            m.add((j, i))
    return(m)

for r in data:
    points = [a.strip() for a in r.split('->')]
    i = 0
    while i in range(len(points)-1):
        themap = draw(themap, points[i], points[i+1])
        i += 1

def pp(m1, m2, f=(500,0)):
    x1 = min(min(m1, key=lambda item:item[0])[0] - 1, min(m2, key=lambda item:item[0])[0] - 1)
    x2 = max(max(m1, key=lambda item:item[0])[0] + 1, max(m2, key=lambda item:item[0])[0] + 1)
    y1 = 0
    y2 = max(themap,key=lambda item:item[1])[1] + 3
    for y in range(y1, y2 + 1):
        row = ''
        for x in range(x1, x2 + 1):
            if (x,y) in m1:
                row += '#'
            elif (x,y) in m2:
                row += 'o'
            elif (x,y) == (500, 0):
                row += '+'
            elif (x,y) == f:
                row += 'v'
            else:
                row += '.'
        print(row)


sand = (500, 0)
sandmap = set()
bottom = max(themap,key=lambda item:item[1])[1]
def sanding(themap, sandmap, floor = False):
    def lookleft(point):
        return((point[0] - 1, point[1] + 1))
    def lookright(point):
        return((point[0] + 1, point[1] + 1))
    def falldown(point):
        return((point[0], point[1] + 1))

    falling = sand
    while True:
        if falling[1] >= bottom and not(floor):
            # The cavity is full, spilling over
            return(len(sandmap))
        elif floor and falling[1] == (bottom + 1):
            # Settling here
            sandmap.add(falling)
            falling = sand
        elif falldown(falling) not in themap and falldown(falling) not in sandmap:
            # Normal fall
            falling = falldown(falling)
        elif (falldown(falling) in themap or falldown(falling) in sandmap) and (lookleft(falling) in themap or lookleft(falling) in sandmap):
            if lookright(falling) in themap or lookright(falling) in sandmap:
                if floor and falling == sand:
                    sandmap.add(falling)
                    return(len(sandmap))
                # Settling here
                sandmap.add(falling)
                falling = sand
            else:
                falling = lookright(falling)
        elif falldown(falling) in themap or falldown(falling) in sandmap:
            falling = lookleft(falling)

print('1:', sanding(themap, sandmap))
pp(themap, sandmap)

print('2:', sanding(themap, sandmap, True))
pp(themap, sandmap)
