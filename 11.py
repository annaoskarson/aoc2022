data = [r.strip() for r in open('11.txt')]

factor = 1

def load():
    global factor
    monkeys = {}
    i = 0
    while i < len(data):
        r = data[i]
        if r.startswith('Monkey'):
            mnum = int(data[i].split( )[1][:-1])
            monkeys[mnum] = {}
            this = monkeys[mnum]
            this['items'] = [int(a) for a in data[i+1].split(' ', 2)[2].split(',')]
            this['op'] = data[i+2].split(' ')[-2:]
            this['test'] = int(data[i+3].split(' ')[-1])
            this['true'] = int(data[i+4].split(' ')[-1])
            this['false'] = int(data[i+5].split(' ')[-1])
            this['seen'] = 0
        i += 1
    factor = 1
    for f in [monkeys[m]['test'] for m in monkeys]:
        factor *= f
    return(monkeys)

def pp(monkeys):
    for m in monkeys:
        print(monkeys[m]['seen'], monkeys[m]['items'])
    print('')

def round(monkeys, divide=True):
    for m in monkeys:
        this = monkeys[m]
        items = this['items']
        this['items'] = []
        for i in items:
            this['seen'] += 1
            if this['op'][1] == 'old':
                num = i
            else:
                num = int(this['op'][1])
            if this['op'][0] == '+':
                new = i + num
            elif this['op'][0] == '*':
                new = i * num
            if divide:
                new = new // 3
            else:
                #print(new)
                new = new % factor
                #print(new, '\n')
            if new % this['test'] == 0:
                monkeys[this['true']]['items'].append(new)
            else:
                monkeys[this['false']]['items'].append(new)

def points(monkeys):
    p = [monkeys[m]['seen'] for m in monkeys]
    p.sort()
    return(p)

monkeys = load()
for t in range(20):
    round(monkeys)
p = points(monkeys)
print('1:', p[-1] * p[-2])

monkeys = load()
for t in range(10000):
    round(monkeys, False)
p = points(monkeys)
print('2:', p[-1] * p[-2])
