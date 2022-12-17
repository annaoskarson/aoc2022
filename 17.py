data = [a.strip() for a in open('17.txt')][0]

def pp(m1, top=False):
    ymax = max(m1, key = lambda t: t[1])[1]
    ymin, xmin, xmax = 0, 0, 8
    ymin = ymax - 20 if top else 0
    
    row = '         '
    print(row, ymax+2)
    for y in range(ymax+1, ymin, -1):
        row = ''
        for x in range(xmin, xmax+1):
            if x in [xmin, xmax]:
                row += '|'
            elif (x, y) in m1:
                row += '#'
            else:
                row += '.'
        print(row, y)
    row = '+-------+'
    if not top:
        print(row, y-1)
    print(' ')

themap = set()
start = [(x,0) for x in range(1, 8)]
themap.update(start)

def move(rock, dx=0): #0 for down, -1 or 1 for side
    if dx == 0:
        rock = [(x, y-1) for (x,y) in rock]
    else:
        rock = [(x+dx, y) for (x,y) in rock]
    return(rock)

def sidecheck(rock):
    return(any((x == 0 or x == 8 for (x,y) in rock)))

rocks = [[(3,1), (4,1), (5,1), (6,1)],
        [(4,3), (3,2), (4,2), (5,2), (4,1)],
        [(5,3), (5,2), (3,1), (4,1), (5,1)],
        [(3,4), (3,3), (3,2), (3,1)],
        [(3,2), (3,1), (4,2), (4,1)]]

def position(m1, r):
    ymax = max(m1, key = lambda t: t[1])[1]
    r = [(x, y+ymax+3) for (x,y) in r]
    return(r)

i = 0
nextrock = -1
times = 0
number = 1000000000000

cycleheight = 0
cyclerocks = 0
baseheight = 0
baserocks = 0

while times < number:

    # Take the next rock
    nextrock = (nextrock+1) % 5
    rock = rocks[nextrock]

    # Place it three rows above the stack! (Or floor.)
    rock = position(themap, rock)

    stuck = False
    while not stuck:
        # Some fiddling with the jet reloading ...
        # Since I noticed that the rock formation is the same
        # each time the jets ar reloading. By eye.
        if i == len(data):
            if baseheight > 0:
                cycleheight = max(themap, key = lambda t: t[1])[1] - baseheight # one full cycle height
                cyclerocks = times - baserocks # one full cycle amount of rocks
                multi = (number - cyclerocks - baserocks) // cyclerocks # The multiplier
                totheight = multi * cycleheight # The added height
                times = multi * cyclerocks + times # Forward in time ...
            if baseheight == 0:
                # Set the base for the whole cycles.
                baseheight = max(themap, key = lambda t: t[1])[1]
                baserocks = times
            i = 0

        # Get the push direction
        d = -1 if data[i] == '<' else 1
        i += 1

        # Push
        pushed = move(rock, d) # First, trying to push
        if sidecheck(pushed) or themap.intersection(set(pushed)):
            #print('could not push')
            pass
        else:       
            #print('push!')     
            rock = move(rock, d)

        # Fall
        falling = move(rock) # First, trying to fall
        if themap.intersection(set(falling)):
            stuck = True
            themap.update(rock)
        else:
            # Fall  
            rock = move(rock)
 
    times += 1
    if times == 2022:
        print('1:', max(themap, key = lambda t: t[1])[1])
        continue

print('2:', totheight + max(themap, key = lambda t: t[1])[1])
