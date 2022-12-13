data = [eval(a.strip()) for a in open('13.txt') if len(a.strip()) > 0]

def comp(left, right):
    if type(right) is list and type(left) is list and len(right) == len(left) == 0:
        return('GO')
    elif type(left) is list and len(left) == 0:
        return(True)
    elif type(right) is list and len(right) == 0:
        return(False)
    elif type(left) is int and type(right) is int:
        if left < right:
            return(True)
        elif left > right:
            return(False)
        else:
            return('GO')
    elif type(left) != type(right):
        if type(left) is int:
            left = [left]
        elif type(right) is int:
            right = [right]
        return(comp(left, right))
    elif type(left) is list and type(right) is list:
        if type(comp(left[0], right[0])) is str:
            return(comp(left[1:], right[1:]))
        else:
            return(comp(left[0], right[0]))

# Part 1
i = 0
p = 0
result = []
while i < len(data):
    p += 1
    l = data[i]
    r = data[i+1]
    i += 2
    if comp(l, r):
        result.append(p)

# Part 2
one, two = [[2]], [[6]]
data.extend([one, two])

Done = False
while not Done:
    i = 0
    tested = []
    Done = True
    while i < len(data)-1:
        if not(comp(data[i], data[i+1])):
            data[i], data[i+1] = data[i+1], data[i]
            Done = False
        i += 1

print('1:', sum(result))
print('2:', (data.index(one)+1) * (data.index(two)+1))
