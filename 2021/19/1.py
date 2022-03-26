import numpy

dir = [
    (0, 1, 2), (0, 1, 2), (0, 2, 1), (0, 2, 1), 
    (0, 1, 2), (0, 1, 2), (0, 2, 1), (0, 2, 1), 
    (1, 0, 2), (1, 0, 2), (1, 2, 0), (1, 2, 0), 
    (1, 0, 2), (1, 0, 2), (1, 2, 0), (1, 2, 0), 
    (2, 1, 0), (2, 1, 0), (2, 0, 1), (2, 0, 1), 
    (2, 1, 0), (2, 1, 0), (2, 0, 1), (2, 0, 1)
]

sign = [
    (+1, +1, +1), (+1, -1, -1), (+1, +1, -1), (+1, -1, +1), 
    (-1, -1, +1), (-1, +1, -1), (-1, -1, -1), (-1, +1, +1), 
    (+1, -1, +1), (+1, +1, -1), (+1, -1, -1), (+1, +1, +1), 
    (-1, +1, +1), (-1, -1, -1), (-1, -1, +1), (-1, +1, -1), 
    (+1, +1, -1), (+1, -1, +1), (+1, +1, +1), (+1, -1, -1), 
    (-1, +1, +1), (-1, -1, -1), (-1, +1, -1), (-1, -1, +1)
]

def transformCoord(T, pos):
    global dir, sign
    return ( T[dir[pos][0]]*sign[pos][0], T[dir[pos][1]]*sign[pos][1], T[dir[pos][2]]*sign[pos][2] )

def overlap(s1, s2, pos):
    global dir, sign
    
    for i in range(len(s1)):
        for j in range(len(s2)):
            #print(scanner[i], transformCoord(scanner[j], pos))
            x, y, z = tuple(numpy.subtract(s1[i], transformCoord(s2[j], pos))) #coordinates of the second scanner
            #x, y, z = tuple( numpy.add(origin, (x,y,z) ) )
            count = 0
            for a,b,c in s2:
                if tuple( numpy.add(transformCoord( (a,b,c), pos), (x,y,z) ) ) in s1:
                    count += 1
            if count >= 12:
                return (x,y,z)
    return None
    

def maxOverlap(s1, s2):
    for i in range(24):
        m = overlap(s1, s2, i)
        if m:
            return (m, i)
    return None
    

nScanner = 0
scanner = []
with open('input.txt', 'r') as f:
    while True:
        line = f.readline() #which scanner
        line = f.readline()
        l = []
        while line.strip():
            x, y, z = line.strip().split(',')
            l.append((int(x), int(y), int(z)))
            line = f.readline()
        scanner.append(l)
        nScanner += 1
        if not line:
            break

visited = [0] * nScanner
scannerPos = [(0,0,0)] * nScanner

Q = set([0])

g = open('output.txt', 'w')
for k in range(len(scanner[0])):
    print(scanner[0][k], file=g)

while not all(visited):
    cur = Q.pop()
    visited[cur] = 1
    for j in range(nScanner):
        if j != cur and not visited[j] and not j in Q:
            res = maxOverlap(scanner[cur], scanner[j])
            if res:
                Q.add(j)
                ((x,y,z), p) = res
                print(f'{j}: {x} {y} {z} {p}')
                scannerPos[j] = (x,y,z)
                #print(f'--- scanner {cur} ---', file=g)
                for k in range(len(scanner[j])):
                    scanner[j][k] = tuple( numpy.add( transformCoord(scanner[j][k], p), (x,y,z) ) )
                    print(scanner[j][k], file=g)

g.close()