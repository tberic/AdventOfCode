import re
import z3

def dist( A, B ):
    return abs(A[0]-B[0]) + abs(A[1]-B[1]) + abs(A[2]-B[2])

def inside(T, C, res=1):
    return C[0] - C[3] <= T[0]*res <= C[0] + C[3] and \
            C[1] - C[3] <= T[1]*res <= C[1] + C[3] and \
            C[2] - C[3] <= T[2]*res <= C[2] + C[3]


f = open('input.txt', 'r')
lines = [line.strip() for line in f]
f.close()

cube = []

minx, miny, minz = 0, 0, 0
maxx, maxy, maxz = 0, 0, 0
maxRadius = 0
minRadius = 10**10
for line in lines:
    m = re.match(r'pos=<(\-?\d+),(\-?\d+),(\-?\d+)>, r=(\d+)', line)
    x, y, z, r = list(map(int, m.groups()))
    cube.append( (x, y, z, r) )
    minx = min(minx, x)
    miny = min(miny, y)
    minz = min(minz, z)
    maxx = max(maxx, x)
    maxy = max(maxy, y)
    maxz = max(maxz, z)
    minRadius = min(minRadius, r)
    maxRadius = max(maxRadius, r)
    

# print(minx, miny, minz)
# print(maxx, maxy, maxz)
# print(minRadius, maxRadius)
# print(len(cube))

offset = 10
maxCount = 977
a, b, c = 0, 0, 0

resolution = 10**7
for x in range(minx//resolution, maxx//resolution+1):
    for y in range(miny//resolution, maxy//resolution+1):
        for z in range(minz//resolution, maxz//resolution+1):
            count = 0
            for k in range(len(cube)):
                if inside( (x, y, z), cube[k], resolution ):
                    count += 1
            if count == maxCount:
                print(x, y, z)
                a, b, c = x, y, z

#print(f'({a}, {b}, {c}) @ resolution {resolution}')

while resolution > 1:
    print(f'({a}, {b}, {c}) @ resolution {resolution}')
    a *= 10
    b *= 10
    c *= 10

    resolution //= 10

    da, db, dc = 0, 0, 0
    for x in range(a-offset, a+offset+1):
        for y in range(b-offset, b+offset+1):
            for z in range(c-offset, c+offset+1):
                count = 0
                for k in range(len(cube)):
                    if inside( (x, y, z), cube[k], resolution ):
                        count += 1
                if count == maxCount:
                    #print(x, y, z)
                    da, db, dc = x, y, z
    
    a, b, c = da, db, dc

    #print(maxCount)
    #print(a, b, c)
    print()

print(a, b, c)