f = open('input.txt', 'r')
line = f.readline().strip()
f.close()

MAXL = 200
delivered = [[0 for i in range(-MAXL, MAXL+1)] for j in range(-MAXL, MAXL+1)]

minx = 0
maxx = 0
miny = 0
maxy = 0
x = 0
y = 0
delivered[0][0] = 1
for c in line:
    # if x > maxx:
    #     maxx = x
    # if x < minx:
    #     minx = x
    # if y > maxy:
    #     maxy = y
    # if y < miny:
    #     miny = y

    if c == 'v':
        y -= 1
    elif c == '^':
        y += 1
    elif c == '<':
        x -= 1
    elif c == '>':
        x += 1

    delivered[x][y] += 1        

count = 0
for i in range(-MAXL, MAXL+1):
    for j in range(-MAXL, MAXL+1):
        if delivered[i][j]:
            count += 1

print(count)