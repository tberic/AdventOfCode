import heapq

def convert(c):
    if (c >= 'a' and c <= 'z'):
        return 1 << (ord(c)-ord('a')+1)
    return 0

def nOnes(x):
    n = 0
    while (x > 0):
        n += x%2
        x //= 2        
    return n

def countKeys():
    global grid, m, n
    cnt = 0
    for y in range(m):
        for x in range(n):
            if (grid[y][x].islower()):
                cnt += 1
    return cnt

def possible(y, x, keys):
    if (y < 0 or y >= m):
        return 0
    if (x < 0 or x >= n): 
        return 0
    if (grid[y][x] == '#'):
        return 0    
    if (grid[y][x] == '.' or grid[y][x] == '@'): 
        return 1
    if (grid[y][x] >= 'a' and grid[y][x] <= 'z'):
        return 1
    if (grid[y][x] >= 'A' and grid[y][x] <= 'Z' and (keys & convert(grid[y][x].lower())) ):
        return 1
    return 0


f = open('input2.txt', 'r')
grid = [line.strip() for line in f]

for line in grid:
    print(line)

m = len(grid)
n = len(grid[0])

def findStart():
    for y in range(m):
        for x in range(n):
            if (grid[y][x] == '@'):
                return (y, x)

(y0, x0) = findStart()

dirs = [ [-1, 0], [+1, 0], [0, -1], [0, +1] ]

Q = []
heapq.heappush( Q, [0, y0, x0, 1] )

nKeys = countKeys()
#print(nOnes(15))
print(nKeys)

while (Q):
    [steps, y, x, keysCollected] = heapq.heappop(Q)
    #print(steps, y, x, keysCollected)

    if (nOnes(keysCollected) == nKeys+1):
        print(steps)
        break

    for i in range(len(dirs)):
        dy = dirs[i][0]
        dx = dirs[i][1]        
        
        if ( possible(y+dy, x+dx, keysCollected) ):
            heapq.heappush(Q, [steps+1, y+dy, x+dx, keysCollected | convert(grid[y+dy][x+dx])] )
   
