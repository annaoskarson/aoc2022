# pydroid3 on phone

data = [r.strip() for r in open('21.txt')]

monkeys = {}
for l in data:
    name, say = l.split(': ')
    monkeys[name] = say

def say(name):
    
    if monkeys[name].isdigit():
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