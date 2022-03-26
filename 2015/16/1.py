import re

sue = { "children": 3, "cats": 7, "samoyeds": 2, "pomeranians": 3, "akitas": 0, \
        "vizslas": 0, "goldfish": 5, "trees": 3, "cars": 2, "perfumes": 1 }

f = open('input.txt', 'r')
for line in f:
    m = re.search(r'Sue (\d+): (.*)', line.strip())
    n, l = m.groups()
    found = 1
    for s in l.split(','):
        x, y = s.split(':')
        x = x.strip()
        y = int(y)
        if sue[x] != y:
            found = 0
            break
    if found:
        print(n)
        break

    

f.close()