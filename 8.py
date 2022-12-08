data = [[int(a) for a in list(r.strip())] for r in open('8.txt')]

def visible(x,y):
    if x in [0, len(data[0])] or y in [0, len(data)]:
        return(True)
    east = all([a < data[y][x] for a in data[y][x+1:]])
    west = all([a < data[y][x] for a in data[y][:x]])
    south = all([a[x] < data[y][x] for a in data[y+1:]])
    north = all([a[x] < data[y][x] for a in data[:y]])
    if any([west, east, north, south]):
        return(True)
 
def scenic(x,y):
    if x in [0, len(data[0])-1] or y in [0, len(data)-1]:
        return(0) # On a border.
    east = [a for a in data[y][x+1:]]
    west = [a for a in data[y][:x][::-1]]
    south = [a[x] for a in data[y+1:]]
    north = [a[x] for a in data[:y][::-1]]
    def view(tree, row):
        for i, t in enumerate(row):
            if t >= tree:
                return(i+1)
        return(len(row))
    score = 1
    for dir in [west, east, north, south]:
        score = score * view(data[y][x], dir)
    return(score)

vis = set()
sc = 0
for y in range(len(data)):
    for x in range(len(data[0])):
        if visible(x,y): # Check if visible
            vis.add((x,y))
        sc = max(sc, scenic(x,y)) # Calculate scenic score
print('1:', len(vis))
print('2:', sc)
