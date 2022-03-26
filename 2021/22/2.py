def overlap1D(line1, line2):
    a = None
    b = None
    if (line2[0] <= line1[0] <= line2[1]):
        a = line1[0]
    elif (line1[0] <= line2[0] <= line1[1]):
        a = line2[0]
    if (line2[0] <= line1[1] <= line2[1]):
        b = line1[1]
    elif (line1[0] <= line2[1] <= line1[1]):
        b = line2[1]
    if a and b:
        return (a, b)
    return None

def overlap3D(cube1, cube2):
    x = overlap1D( (cube1[0], cube1[1]), (cube2[0], cube2[1]) )
    y = overlap1D( (cube1[2], cube1[3]), (cube2[2], cube2[3]) )
    z = overlap1D( (cube1[4], cube1[5]), (cube2[4], cube2[5]) )
    if x and y and z:
        return (x[0], x[1], y[0], y[1], z[0], z[1])
    return None

def sign(x):
    if x % 2:
        return 1
    return -1

def vol(c):
    return (c[1]-c[0]+1)*(c[3]-c[2]+1)*(c[5]-c[4]+1)*c[6]

import re
f = open('input.txt', 'r')
l = []
i = 0
for line in f:
    m = re.match(r'^(.*)\sx=(\-?\d+)\.\.(\-?\d+),y=(\-?\d+)\.\.(\-?\d+),z=(\-?\d+)\.\.(\-?\d+)$', line)
    command,x1,x2,y1,y2,z1,z2 = m.groups()
    x1,x2,y1,y2,z1,z2 = list(map(int, m.groups()[1:]))
    if command == "on":
        val = 1
    else:
        val = 0
    l.append((x1, x2, y1, y2, z1, z2, val, 1)) #the last coordinate denotes the number of overlaps with all cubes (actually, the sign)
    i += 1
f.close()

cube = []
for i in range(len(l)):
    #if not l[i][6]: #if it is off, don't do anything
    #    continue
    for j in range(len(cube)):
        c = overlap3D(l[i], cube[j])
        if c: #there is an overlap and we will add the overlapping cube to the end of the list cube
                cube.append( ( c[0], c[1], c[2], c[3], c[4], c[5], -cube[j][6] ) )
    if l[i][6]:
        cube.append( ( l[i][0], l[i][1], l[i][2], l[i][3], l[i][4], l[i][5], 1 ) )

sum = 0
for c in cube:
    sum += vol(c)

print(sum)