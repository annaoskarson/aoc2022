data = [r.strip() for r in open('7.txt')]

pwd = [] # working directory
ds = {} # The size of directories
ls = set() # which ones have been listed
for i,row in enumerate(data):
    if row.startswith('$ ls'):
        ls.add('/'.join(pwd))
        j = i + 1
        while j < len(data) and not(data[j].startswith('$')):
            size, name = data[j].split(' ')
            if size != 'dir':
                for i,d in enumerate(pwd):
                    df = '/'.join(pwd[:i+1])
                    if df not in ds:
                        ds[df] = 0
                    ds[df] += int(size)
            j += 1
    elif row.startswith('$ cd'):
        d = row.split(' ')[2]
        if d == '/':
            pwd = ['/']
        elif d == '..':
            _ = pwd.pop()
        else:
            pwd.append(d)
a = sum([sz for sz in ds.values() if sz <= 100000])
print('1:', a)

avail = 70000000 - ds['/']
need = 30000000
delete = need - avail
sds = dict(sorted(ds.items(), key=lambda item: item[1]))

for x in sds:
    if sds[x] > delete:
        print('2:', sds[x]) #First one just enough large.
        break
