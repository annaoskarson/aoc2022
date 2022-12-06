data = [r.strip() for r in open('6.txt')][0]
found = False
i = 3
afound = False

while not(found):
    
    if not(afound) and len(set(list(data[i-3:i+1]))) == 4:
        a = i+1
        afound = True

    if i >= 13 and len(set(list(data[i-13:i+1]))) == 14:
        b = i+1
        found = True

    i += 1

print("1:", a) 
print("2:", b)   