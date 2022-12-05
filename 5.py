data = [r.rstrip() for r in open('5.txt')]

stacksI = {}
stacksII = {}
start = data.index('')

i = start - 1
numbers = [int(n.strip()) for n in data[i].split(' ') if len(n.strip()) > 0 ]
for n in numbers:
    stacksI[n] = []
    stacksII[n] = []
while i > 0:
    i -= 1
    s = data[i][1::4]
    for n,box in enumerate(s):
        if box != ' ':
            stacksI[n+1].append(box)
            stacksII[n+1].append(box)

i = start + 1
while i < len(data):
    [amount, fr, to] = [int(d) for d in data[i].split(' ')[1::2]]
    stacksI[to].extend(reversed(stacksI[fr][-amount:]))
    stacksI[fr] = stacksI[fr][:-amount]
    stacksII[to].extend(stacksII[fr][-amount:])
    stacksII[fr] = stacksII[fr][:-amount]
    i += 1

print('1:', ''.join([stacksI[s][-1] for s in stacksI]))
print('2:', ''.join([stacksII[s][-1] for s in stacksII]))