# pydroid3 on phone

data = [r.strip() for r in open('21.txt')]

monkeys = {}
for l in data:
    name, say = l.split(': ')
    monkeys[name] = say

def say(name):
    
    if monkeys[name].lstrip('-').isdigit():
        return(int(monkeys[name]))
    else:
        wait = monkeys[name]
        if len(wait.split(' ')) > 1:
            m1, op, m2 = wait.split(' ')
            if op == '+':
                return(say(m1) + say(m2))
            elif op == '*':
                return(say(m1) * say(m2))
            elif op == '/':
                return(say(m1) // say(m2))
            elif op == '-':
                return(say(m1) - say(m2))
            else:
                assert False
        else:
            return(monkeys[wait])

print('1:', say('root'))

# Continuing on computer
# Looked at some trials and found:
#   - If first monkey in pair is smaller, we need to decrease x
#   - Start on a random high number
#   - No need for negative x:es

m1, _,  m2 = monkeys['root'].split(' ')
x = 100000000000000
dx = -(-x // 2) # Ceiling division
while True:
    monkeys['humn'] = str(x)
    m1v, m2v = say(m1), say(m2)
    if m1v == m2v:
        break
    if m1v < m2v:
        x -= dx
    else:
        x += dx
    dx = -(-dx // 2) # Ceiling division    

print('2:', x)