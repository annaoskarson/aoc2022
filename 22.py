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

pp(M, path)

p1 = 1000 * (me[0][1] + 1) + 4 * (me[0][0] + 1) + me[1]
print('1:', p1)
