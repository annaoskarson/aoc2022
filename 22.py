data = [r.strip('\n') for r in open('22.txt')]
com = data[-1]
data = data[:-2]

maxX = max([len(l) for l in data])
maxY = len(data)

def buildmap(data):
    M = {} # The map content
    for y in range(maxY):
        for x in range(maxX):
            if x >= len(data[y]):
                M[(x,y)] = ' '
            else:
                M[(x,y)] = data[y][x]
    return(M)

def onestepcube(me):
    coord, d = me
    (x,y) = coord
    # A down
    if d == 1 and y == 49 and x >= 100:
        return((99, x - 50), 2) #
    # A right
    elif d == 0 and x == 99 and 50 <= y < 100:
        return((y + 50, 49), 3) #
    # B right (upper)
    elif d == 0 and x == 149:
        return((99, 149 - y), 2) #
    # B right (lower)
    elif d == 0 and x == 99 and 100 <= y < 150:
        return((149, 149 - y), 2) #
    # C down
    elif d == 1 and y == 149 and 50 <= x < 100:
        return((49, x + 100), 2) #
    # C right
    elif d == 0 and x == 49 and 150 <= y < 200:
        return((y - 100 , 149), 3) #
    # D up
    elif d == 3 and y == 100 and x < 50:
        return((50, 50 + x), 0) #
    # D left
    elif d == 2 and x == 50 and 50 <= y < 100:
        return((y - 50, 100), 1) #
    # E left (upper)
    elif d == 2 and x == 50 and y < 50:
        return((0, 149 - y), 0) #
    # E left (lower)
    elif d == 2 and x == 0 and y < 150:
        return((50, 149 - y), 0) #
    # F up
    elif d == 3 and y == 0 and 50 <= x < 100 :
        return((0, x + 100), 0) #
    # F left
    elif d == 2 and x == 0 and y >= 150:
        return((y - 100, 0), 1)
    # G up
    elif d == 3 and y == 0 and x >= 100:
        return((x - 100, 199), 3)
    # G down
    elif d == 1 and y == 199:
        return((x + 100, 0), 1)
    else:
        if d == 0:
            return((x+1, y), d)
        elif d == 1:
            return((x, y+1), d)
        elif d == 2:
            return((x-1, y), d)
        elif d == 3:
            return((x, y-1), d)
# Facing is 0 for right (>), 1 for down (v), 2 for left (<), and 3 for up (^)

def walkcube(me, op):
    pos, face = me
    x, y = pos
    global path
    if not op.isnumeric():
        # Time to turn.
        if op == 'R':
            face = (face + 1) % 4
        elif op == 'L':
            face = (face + 3) % 4        
        path[pos] = face
        me = (pos, face)
        return(me)
    step = 0
    while step < int(op):
        coords, face1 = onestepcube(((x,y), face))
        x1, y1 = coords
        if M[(x1, y1)] == '#':
            # End here.
            return(((x,y), face))
        elif M[(x1, y1)] == '.':
            # Can go here.
            path[(x1, y1)] = face
            x, y = x1, y1
            face = face1
            step += 1
            pass
        else:
            print((x,y), face, (x1,y1), face1)
            print(M[(x,y)], M[(x1,y1)])
            assert False
    me = ((x,y), face)
    return(me)

def pp(themap, path):
    for y in range(maxY):
        line = ''
        for x in range(maxX):
            if (x,y) in path.keys():
                line += ['>','v','<','^'][path[(x,y)]]
            else:
                line += themap[(x,y)]
        print(line, y)
    print('')

M = buildmap(data)
startx = min([x for x in range(0, maxX) if  M[(x,0)] == '.'])
me = ((startx, 0), 0)
path = {(startx, 0): 0}
#pp(M, path)

# Facing is 0 for right (>), 1 for down (v), 2 for left (<), and 3 for up (^)
def walk(me, op):
    def onestep(me):
        pos, face = me
        x, y = pos
        if face == 0:
            x, y = x+1, y
        elif face == 1:
            x, y = x, y+1
        elif face == 2:
            x, y = x-1, y
        elif face == 3:
            x, y = x, y-1
        x = x % maxX
        y = y % maxY
        me = ((x,y), face)
        return(me)

    global path
    pos, face = me
    x, y = pos
    if not op.isnumeric():
        # Time to turn.
        if op == 'R':
            face = (face + 1) % 4
        elif op == 'L':
            face = (face + 3) % 4        
        path[pos] = face
        me = (pos, face)
        return(me)
    step = 0
    while step < int(op):
        me1, _ = onestep(((x,y), face))
        x1, y1 = me1
        if M[(x1, y1)] == '#':
            # End here.
            return(((x,y), face))
        elif M[(x1, y1)] == '.':
            # Can go here.
            path[(x1, y1)] = face
            x, y = x1, y1
            step += 1
            pass
        else:
            # We reached whitespace.
            xt, yt = x1, y1
            while M[(xt, yt)] == ' ':
                met, _ = onestep(((xt, yt), face))
                xt, yt = met
            if M[(xt, yt)] == '#':
                # End here
                path[(x, y)] = face
                return(((x,y), face))
            elif M[(xt,yt)] == '.':
                x, y = xt, yt
                path[(x, y)] = face
                step += 1
            else:
                assert False
    me = ((x,y), face)
    return(me)

i = 0
c = ''
while i < len(com):
    if com[i].isnumeric():
        while i < len(com) and com[i].isnumeric():
            c += com[i]
            i += 1
    else:
        c = com[i]
        i += 1
    me = walk(me, c)
    c = ''

#pp(M, path)

p1 = 1000 * (me[0][1] + 1) + 4 * (me[0][0] + 1) + me[1]
print('1:', p1)


M = buildmap(data)
startx = min([x for x in range(0, maxX) if  M[(x,0)] == '.'])
me = ((startx, 0), 0)
path = {(startx, 0): 0}
#pp(M, path)

i = 0
c = ''
while i < len(com):
    if com[i].isnumeric():
        while i < len(com) and com[i].isnumeric():
            c += com[i]
            i += 1
    else:
        c = com[i]
        i += 1
    me = walkcube(me, c)
    c = ''

#pp(M, path)

p2 = 1000 * (me[0][1] + 1) + 4 * (me[0][0] + 1) + me[1]
print('2:', p2)
# 32468 too low
# 55288 wrong
# 78276 too high