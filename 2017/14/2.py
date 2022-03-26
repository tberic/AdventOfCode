def denseHash(a):
    h = []
    for i in range(16):
        s = 0
        for j in range(16):
            s ^= a[ 16*i+j ]
        h.append(s)
    return h            

def knot(a, pos, n):
    if pos + n < len(a):
        return a[:pos] + a[pos:pos+n][::-1] + a[pos+n:]
    
    b = (a[pos:] + a[:(pos+n)%len(a)])[::-1]
    return b[len(a)-pos:] + a[ (pos+n)%len(a):pos ] + b[ :len(a)-pos ]

def knotHash(a, l, pos=0, skip=0):
    for n in l:
        a = list(knot(a, pos, n))
        pos = (pos + n + skip) % len(a)
        skip += 1
    return (a, pos, skip)

def hash(s):
    lengths = [ ord(c) for c in s ]
    lengths = lengths + [17, 31, 73, 47, 23]
    a = list(range(256))
    pos = 0
    skip = 0
    for _ in range(64):
        a, pos, skip = knotHash( a, lengths, pos, skip )

    res = ""
    for x in denseHash(a):
        res += (str(hex(x))[2:]).zfill(2)
    
    return res

def row(s):
    a = []
    for c in s:
        a += ( [int(c) for c in bin(int(c, 16))[2:].zfill(4)] )
    return a

def floodFill(x, y):
    global grid, visited
    if x < 0 or x >= len(grid):
        return
    if y < 0 or y >= len(grid):
        return

    if not grid[x][y]:
        return

    if visited[x][y]:
        return

    visited[x][y] = 1
    floodFill(x-1, y)
    floodFill(x+1, y)
    floodFill(x, y-1)
    floodFill(x, y+1)


s = "xlqgujun"
grid = []
for i in range(128):
    #print( hash(s+'-'+str(i)) )
    grid.append( row( hash(s+'-'+str(i)) ) )

visited = [[0 for j in range(len(grid[i]))] for i in range(len(grid))]

regions = 0
for i in range(len(grid)):
    for j in range(len(grid[i])):
        if grid[i][j] and not visited[i][j]:
            regions += 1
            floodFill(i, j)
print(regions)