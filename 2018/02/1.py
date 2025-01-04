import string

f = open('input.txt', 'r')

ntwos = 0
nthrees = 0
for line in f:
    twos = False
    threes = False
    for c in string.ascii_lowercase:
        s = 0
        for x in line.strip():
            if x == c:
                s += 1
        if s == 2:
            twos = True
        if s == 3:
            threes = True

    if twos:
        ntwos += 1
    if threes:
        nthrees += 1

print(ntwos*nthrees)

f.close()