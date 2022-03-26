import re

def dist( A, B ):
    return abs(A[0]-B[0]) + abs(A[1]-B[1]) + abs(A[2]-B[2])

def intersection1D( A, B ):
    if A[0] <= B[0] <= A[1]:
        return ( B[0], min(B[1], A[1]) )
    if B[0] <= A[0] <= B[1]:
        return ( A[0], min(A[1], B[1]) )
    return None

def intersection( A, B ):
    s1 = intersection1D( (A[0], A[3]), (B[0], B[3]) )
    s2 = intersection1D( (A[1], A[4]), (B[1], B[4]) )
    s3 = intersection1D( (A[2], A[5]), (B[2], B[5]) )

    if not s1 or not s2 or not s3:
        return None

    return ( s1[0], s2[0], s3[0], s1[1], s2[1], s3[1] )

def inside(T, C, res=1):
    return C[0] <= T[0]*res <= C[3] and C[1] <= T[1]*res <= C[4] and C[2] <= T[2]*res <= C[5]

def scale(C, res):
    return ( C[0]//res, C[1]//res, C[2]//res, C[3]//res, C[4]//res, C[5]//res )


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
    cube.append( (x-r, y-r, z-r, x+r, y+r, z+r) )
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

resolution = 10**7
maxCount = 0
for x in range(minx//resolution, maxx//resolution+1):
    for y in range(miny//resolution, maxy//resolution+1):
        for z in range(minz//resolution, maxz//resolution+1):
            count = 0
            for k in range(len(cube)):
                if inside( (x, y, z), cube[k], resolution ):
                    count += 1
            if count > maxCount:
                maxCount = count
                a, b, c = x, y, z

#print(f'({a}, {b}, {c}) @ resolution {resolution}')

while resolution > 1:
    print(f'({a}, {b}, {c}) @ resolution {resolution}')    
    a *= 10
    b *= 10
    c *= 10

    resolution //= 10

    # print('Boundaries: ')
    # print(minx//resolution, miny//resolution, minz//resolution)
    # print(maxx//resolution, maxy//resolution, maxz//resolution)
    # print(minRadius//resolution, maxRadius//resolution)

#    scaledCube = [scale(c, resolution) for c in cube]
    
    maxCount = 0
    da, db, dc = 0, 0, 0
    for x in range(a-offset, a+offset+1):
        for y in range(b-offset, b+offset+1):
            for z in range(c-offset, c+offset+1):
                count = 0
                for k in range(len(cube)):
                    if inside( (x, y, z), cube[k], resolution ):
                        count += 1
                if count > maxCount:
                    maxCount = count
                    da, db, dc = x, y, z
    
    a, b, c = da, db, dc

    print(maxCount)
    #print(a, b, c)
    print()

    print(a, b, c)