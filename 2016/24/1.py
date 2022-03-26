import heapq
from itertools import permutations

f = open('input.txt', 'r')
grid = [list(line.strip()) for line in f]
f.close()

m = len(grid)
n = len(grid[0])

pos = [(0, 0) for i in range(10)]

N = 0
#find the numbered nodes
for i in range(m):
    for j in range(n):
        if grid[i][j] in '0123456789':
            pos[ int(grid[i][j]) ] = (i, j)
            if int(grid[i][j]) > N:
                N = int(grid[i][j])
            grid[i][j] = '.'

distPair = [[0 for j in range(N+1)] for i in range(N+1)]

inf = 10**10            
#we run dijkstra for each of the numbered nodes
for k in range(N+1):
    Q = []
    dist = [ [inf for j in range(n)] for i in range(m) ]
    visited = [ [0 for j in range(n)] for i in range(m) ]
    heapq.heappush( Q, (0, pos[k]) )
    dist[ pos[k][0] ][ pos[k][1] ] = 0

    while Q:
        _, (x, y) = heapq.heappop(Q)
        visited[x][y] = 1

        if (x > 0 and grid[x-1][y] == '.' and not visited[x-1][y]):
            if dist[x][y] + 1 < dist[x-1][y]:
                dist[x-1][y] = dist[x][y] + 1
                heapq.heappush( Q, (dist[x][y] + 1, (x-1, y)) )
        if (x < m-1 and grid[x+1][y] == '.' and not visited[x+1][y]):
            if dist[x][y] + 1 < dist[x+1][y]:
                dist[x+1][y] = dist[x][y] + 1
                heapq.heappush( Q, (dist[x][y] + 1, (x+1, y)) )
        if (y > 0 and grid[x][y-1] == '.' and not visited[x][y-1]):
            if dist[x][y] + 1 < dist[x][y-1]:
                dist[x][y-1] = dist[x][y] + 1
                heapq.heappush( Q, (dist[x][y] + 1, (x, y-1)) )
        if (y < n-1 and grid[x][y+1] == '.' and not visited[x][y+1]):
            if dist[x][y] + 1 < dist[x][y+1]:
                dist[x][y+1] = dist[x][y] + 1
                heapq.heappush( Q, (dist[x][y] + 1, (x, y+1)) )

    for l in range(N+1):
        distPair[k][l] = dist[ pos[l][0] ][ pos[l][1] ]

print(N)
print(distPair)
minDist = inf
for p in permutations(range(1, N+1)):
    q = [0] + list(p)
    d = 0
    for k in range(len(q)-1):
        d += distPair[q[k]][q[k+1]]
    if d < minDist:
        minDist = d
        print(q)

print(minDist)