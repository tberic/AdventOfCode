import re

def dist( A, B ):
    return abs(A[0]-B[0]) + abs(A[1]-B[1]) + abs(A[2]-B[2])

f = open('input.txt', 'r')
lines = [line.strip() for line in f]
f.close()

minx, miny, minz = 0, 0, 0
maxx, maxy, maxz = 0, 0, 0
a, b, c = 0, 0, 0
maxRadius = 0
for line in lines:
    m = re.match(r'pos=<(\-?\d+),(\-?\d+),(\-?\d+)>, r=(\d+)', line)
    x, y, z, r = list(map(int, m.groups()))
    minx = min(minx, x)
    miny = min(miny, y)
    minz = min(minz, z)
    maxx = max(maxx, x)
    maxy = max(maxy, y)
    maxz = max(maxz, z)
    if r > maxRadius:
        maxRadius = r
        a, b, c = x, y, z

count = 0
for line in lines:
    m = re.match(r'pos=<(\-?\d+),(\-?\d+),(\-?\d+)>, r=(\d+)', line)
    x, y, z, r = list(map(int, m.groups()))
    if dist( (x, y, z), (a, b, c) ) <= maxRadius:
        count += 1

print(count)
print(minx, miny, minz)
print(maxx, maxy, maxz)