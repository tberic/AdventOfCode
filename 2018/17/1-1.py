import re

f = open('input2.txt', 'r')
#minx, maxx, miny, maxy = 455, 474, 236, 236
minx, maxx, miny, maxy = 495, 495, 2, 7
for line in f:
    m = re.match(r'(.)=(\-?\d+), (.)=(\-?\d+)..(\-?\d+)', line.strip())
    c, a, d, b1, b2 = m.groups()
    if c == 'x':
        minx = min(minx, int(a))
        maxx = max(maxx, int(a))
    elif c == 'y':
        miny = min(miny, int(a))
        maxy = max(maxy, int(a))

    if d == 'x':
        minx = min(minx, int(b1))
        maxx = max(maxx, int(b2))
    elif d == 'y':
        miny = min(miny, int(b1))
        maxy = max(maxy, int(b2))

    #print(c, a, d, b1, b2)
f.close()

#print(minx, maxx, miny, maxy)
grid = [['.' for x in range(maxx-minx+1)]for y in range(maxy-miny+1)]

f = open('input2.txt', 'r')
for line in f:
    m = re.match(r'(.)=(\-?\d+), (.)=(\-?\d+)..(\-?\d+)', line.strip())
    c, a, d, b1, b2 = m.groups()
    
    if c == 'x':
        for i in range(int(b1), int(b2)+1):
            grid[i-miny][int(a)-minx] = '#'
    if c == 'y':
        for i in range(int(b1), int(b2)+1):
            grid[int(a)-miny][i-minx] = '#'
f.close()

g = open('output2.txt', 'w')
for row in grid:
    print("".join(row), file=g)
print(minx, miny, file=g)
g.close()