# Coded in pydroid3 on my phone

data = [r.strip().split() for r in open('10.txt')]

x = 1

def check(x, cycle):
    if cycle in [20, 60, 100, 140, 180, 220]:
        return(x*cycle)
    else:
        return(0)

def sprite(x):
    return([x-1,x,x+1])
    
def pp(cycle, x, screen):
    if cycle % 40 == 1:
        screen.append('')
    cycle = cycle % 40
    if cycle in sprite(x+1):
        screen[-1] += 'M'
    else:
        screen[-1] += ' '
    return(screen)
                        
s=0
cycle = 1
screen = ['']
for i,row in enumerate(data):
    if row[0] == 'noop':
        pass
        s += check(x,cycle)
        screen = pp(cycle, x, screen)
        cycle += 1
    else:
        com, num = row[0], int(row[1])
        s += check(x,cycle)
        screen = pp(cycle, x, screen)
        cycle += 1
        s += check(x,cycle)
        screen = pp(cycle, x, screen)
        x += num
        cycle += 1
        
print('1:', s)
print('2:')
for r in screen:
    print(r)
