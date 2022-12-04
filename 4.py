data = [r.strip() for r in open('4.txt')]

n, m = 0, 0
for row in data:
    e1,e2 = row.split(',')
    [e1a,e1b] = [int(e) for e in e1.split('-')]
    [e2a,e2b] = [int(e) for e in e2.split('-')]
    
    inner = (max(e1a, e2a), min(e1b, e2b))
    if inner in [(e1a, e1b), (e2a, e2b)]:
        n += 1

    if not(e1a > e2b or e2a > e1b):
        m += 1

print("1:", n) 
print("2:", m)   