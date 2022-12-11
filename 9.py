data = [a.strip().split(' ') for a in open('9.txt')]

def follow(hpos, tpos):
    if (abs(hpos[0] - tpos[0])) > 1 or (abs(hpos[1] - tpos[1]) > 1):
        if hpos[0] < tpos[0]:
            tpos[0] -= 1
        elif hpos[0] > tpos[0]:
            tpos[0] += 1
        if hpos[1] < tpos[1]:
            tpos[1] -= 1
        elif hpos[1] > tpos[1]:
            tpos[1] += 1
    return(tpos)

def wiggle(r, d):      
    if d == 'U':
        r[0][1] -= 1
    elif d == 'D':
        r[0][1] += 1
    elif d == 'R':
        r[0][0] += 1
    elif d == 'L':
        r[0][0] -= 1
    # The tail will follow the head.
    i = 1
    while i < len(r):
        r[i] = follow(r[i-1], r[i])
        i += 1
    return(r)

rope = [[0,0] for _ in range(10)]
vis1 = {(0,0)}
vis2 = {(0,0)}
for [d, st] in data:
    for s in range(int(st)):
        rope = wiggle(rope, d)
        vis1.add(tuple(rope[1]))
        vis2.add(tuple(rope[-1]))

print('1:', len(vis1))
print('2:', len(vis2))
