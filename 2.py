data = [l.strip() for l in open('2.txt')]

points = 0
for row in data:
    you, me = row.split(' ')
    if me == 'X':
        points += 1
    elif me == 'Y':
        points += 2
    elif me == 'Z':
        points += 3
    if you == 'A' and me == 'Y':
        points += 6
    elif you == 'A' and me == 'X':
        points += 3
    elif you == 'B' and me == 'Y':
        points += 3
    elif you == 'B' and me =='Z':
        points += 6
    elif you == 'C' and me == 'X':
        points += 6
    elif you == 'C' and me == 'Z':
        points += 3

print('1:', points)

points = 0
for row in data:
    you, strat = row.split(' ')
    if strat == 'X': # lose
        if you == 'A':
            points += 3
        elif you == 'B':
            points += 1
        elif you == 'C':
            points += 2
    elif strat == 'Y': #draw
        if you == 'A':
            points += 1 + 3
        elif you == 'B':
            points += 2 + 3
        elif you == 'C':
            points += 3 + 3
    elif strat == 'Z': #win
        if you == 'A':
            points += 2 + 6
        elif you == 'B':
            points += 3 + 6
        elif you == 'C':
            points += 1 + 6

print('2:', points)
