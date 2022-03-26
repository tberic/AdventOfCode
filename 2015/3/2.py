f = open('input.txt', 'r')
line = f.readline().strip()
f.close()

MAXL = 200
delivered = [[0 for i in range(-MAXL, MAXL+1)] for j in range(-MAXL, MAXL+1)]

# minx = 0
# maxx = 0
# miny = 0
# maxy = 0
x1 = 0
y1 = 0
x2 = 0
y2 = 0
delivered[0][0] = 2
for i in range(len(line)):
    # if x1 > maxx:
    #     maxx = x1
    # if x1 < minx:
    #     minx = x1
    # if y1 > maxy:
    #     maxy = y1
    # if y1 < miny:
    #     miny = y1
    # if x2 > maxx:
    #     maxx = x2
    # if x2 < minx:
    #     minx = x2
    # if y2 > maxy:
    #     maxy = y2
    # if y2 < miny:
    #     miny = y2

    c = line[i]
    if i%2 == 0:
        if c == 'v':
            y1 -= 1
        elif c == '^':
            y1 += 1
        elif c == '<':
            x1 -= 1
        elif c == '>':
            x1 += 1
        delivered[x1][y1] += 1
    else:
        if c == 'v':
            y2 -= 1
        elif c == '^':
            y2 += 1
        elif c == '<':
            x2 -= 1
        elif c == '>':
            x2 += 1
        delivered[x2][y2] += 1

#print(minx, maxx, miny, maxy) 

count = 0
for i in range(-MAXL, MAXL+1):
    for j in range(-MAXL, MAXL+1):
        if delivered[i][j]:
            count += 1

print(count)