data = [r.strip() for r in open('3.txt')]
score = 0
for row in data:
    s = [item for item in    row[:len(row)//2] if item in row[len(row)//2:]][0]
    if ord(s) < 91:
        val = ord(s) - 38
    else:
        val = ord(s) - 96
    score += val
print("1:",score)

score = 0
i = 0
while i < len(data):
    [r1, r2, r3] = data[i:i+3]
    b = [item for item in r1 if item in r2 and item in r3][0]
    if ord(b) < 91:
        val = ord(b) - 38
    else:
        val = ord(b) - 96
    score += val
    i += 3
print("2:",score)