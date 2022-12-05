data = [r.rstrip() for r in open('5.txt')]

stacks = {}
stacksb = {}
i = 0
while i in range(len(data)):
    row = data[i]
    if len(row) == 0:
        start = i
        numbers = [int(n.strip()) for n in data[i-1].split(' ') if len(n.strip()) > 0 ]
        for n in numbers:
            stacks[n] = []
            stacksb[n] = []
        i -= 1
        while i > 0:
            i -= 1
            s = data[i][1::4]
            for n,box in enumerate(s):
                if box != ' ':
                    stacks[n+1].append(box)
                    stacksb[n+1].append(box)
        i = start + 1
        while i < len(data):
            [amount, fr, to] = [int(d) for d in data[i].split(' ')[1::2]]
            stacks[to].extend(reversed(stacks[fr][-amount:]))
            stacksb[to].extend(stacksb[fr][-amount:])
            stacks[fr] = stacks[fr][:-amount]
            stacksb[fr] = stacksb[fr][:-amount]

            i += 1

    i += 1

print('1:', ''.join([stacks[s][-1] for s in stacks]))
print('2:', ''.join([stacksb[s][-1] for s in stacksb]))