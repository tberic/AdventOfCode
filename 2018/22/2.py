import heapq

Erosion = {}

def erosionLevel(index):
    global depth
    return (index + depth) % 20183

def erosion(y, x):
    global targetx, targety
    if (y, x) in Erosion:
        return Erosion[(y, x)]
    
    if y == 0:
        Erosion[(y, x)] = erosionLevel( x*16807 )
        return Erosion[(y, x)]

    if x == 0:
        Erosion[(y, x)] = erosionLevel( y*48271 )
        return Erosion[(y, x)]

    if x == targetx and y == targety:
        Erosion[(y, x)] = erosionLevel( 0 )
        return Erosion[(y, x)]

    Erosion[(y, x)] = erosionLevel( erosion(y-1, x) * erosion(y, x-1) )
    return Erosion[(y, x)]

def grid(y, x):
    return erosion(y, x) % 3


Best = {}

def best(y, x, eq):
    if (y, x, eq) in Best:
        return Best[(y, x, eq)]
    return 10**10



depth = 6969
targetx = 9
targety = 796

# depth = 510
# targetx = 10
# targety = 10

NONE = 1
TORCH = 2
CLIMB = 4

dirs = [(-1, 0), (+1, 0), (0, -1), (0, +1)]
eqs = [ [TORCH, CLIMB], [NONE, CLIMB], [TORCH, NONE] ]

Q = []
heapq.heappush(Q, (0, 0, 0, TORCH) ) # minutes, x, y, equipment

Best[(0, 0, TORCH)] = 0

while Q:
    d, x, y, eq = heapq.heappop(Q)

    #print(d, y, x, eq)

    if x == targetx and y == targety and eq == TORCH:
        print(d)
        break

    for dir in dirs:
        if y+dir[0] >= 0 and x+dir[1] >= 0:
            if eq in eqs[ grid(y+dir[0], x+dir[1]) ] and d + 1 < best(y+dir[0], x+dir[1], eq):
                Best[(y+dir[0], x+dir[1], eq)] = d + 1
                heapq.heappush(Q, (d+1, x+dir[1], y+dir[0], eq))

    other = eqs[ grid(y, x) ][  1 - eqs[grid(y, x)].index(eq)  ]
    if d + 7 < best(y, x, other):
        Best[(y, x, other)] = d + 7
        heapq.heappush(Q, (d+7, x, y, other ))