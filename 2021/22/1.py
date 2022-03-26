import re
f = open('input.txt', 'r')

MAXL = 50
grid = [[[0 for i in range(-MAXL, MAXL+1)] for j in range(-MAXL, MAXL+1)] for k in range(-MAXL, MAXL+1)]

for line in f:
    m = re.match(r'^(.*)\sx=(\-?\d+)\.\.(\-?\d+),y=(\-?\d+)\.\.(\-?\d+),z=(\-?\d+)\.\.(\-?\d+)$', line)
    command,x1,x2,y1,y2,z1,z2 = m.groups()
    x1,x2,y1,y2,z1,z2 = list(map(int, m.groups()[1:]))
    #print(x1,x2,y1,y2,z1,z2)
    if x1 < -MAXL or x2 > MAXL or y1 < -MAXL or y2 > MAXL or z1 < -MAXL or z2 > MAXL:
        continue
    if command == "on":
        val = 1
    else:
        val = 0
    for x in range(x1, x2+1):
        for y in range(y1, y2+1):
            for z in range(z1, z2+1):
                grid[x][y][z] = val
                
count = 0
for x in range(-MAXL, MAXL+1):
    for y in range(-MAXL, MAXL+1):
        for z in range(-MAXL, MAXL+1):
            count += grid[x][y][z]
print(count)

f.close()