from collections import defaultdict

def countPaths(y, x, dir):
    if y == startY and x == startX and dir == startDir:
        return 
    
    visited[y][x] = 1

    for y_, x_, dir_ in parent[(y, x, dir)]:
        countPaths(y_, x_, dir_)

DIRS = [
    [0, +1],
    [-1, 0],
    [0, -1],
    [+1, 0]
]

STRAIGHT = 0
CCW = 1
CW = 2

f = open('input.txt')

grid = [line.strip() for line in f]

for y in range(len(grid)):
    for x in range(len(grid[0])):
        if grid[y][x] == 'S':
            startY, startX = y, x
        if grid[y][x] == 'E':
            endY, endX = y, x

# modified BFS to find all minimum paths
Q = []
startDir = 0
Q.append([startY, startX, startDir])
parent = defaultdict(list)
parent[(startY, startX, startDir)].append(-1)

dist = [[[10 ** 10 for k in range(4)] for j in range(len(grid[0]))] for i in range(len(grid))]
dist[startY][startX][startDir] = 0

while Q:
    y, x, dir = Q.pop(0)

    if grid[y][x] == '#':
        continue

    if dist[y+DIRS[dir][0]][x+DIRS[dir][1]][dir] > dist[y][x][dir] + 1:
        dist[y+DIRS[dir][0]][x+DIRS[dir][1]][dir] = dist[y][x][dir] + 1
        Q.append([y+DIRS[dir][0], x+DIRS[dir][1], dir])
        parent[ (y+DIRS[dir][0], x+DIRS[dir][1], dir) ].clear()
        parent[ (y+DIRS[dir][0], x+DIRS[dir][1], dir) ].append( (y, x, dir) )
    elif dist[y+DIRS[dir][0]][x+DIRS[dir][1]][dir] == dist[y][x][dir] + 1:
        parent[ (y+DIRS[dir][0], x+DIRS[dir][1], dir) ].append( (y, x, dir) )

    if dist[y][x][(dir + 1) % 4] > dist[y][x][dir] + 1000:
        dist[y][x][(dir + 1) % 4] = dist[y][x][dir] + 1000
        Q.append([y, x, (dir + 1) % 4])
        parent[ (y, x, (dir + 1) % 4) ].clear()
        parent[ (y, x, (dir + 1) % 4) ].append( (y, x, dir) )
    elif dist[y][x][(dir + 1) % 4] == dist[y][x][dir] + 1000:
        parent[ (y, x, (dir + 1) % 4) ].append( (y, x, dir) )

    if dist[y][x][(dir + 3) % 4] > dist[y][x][dir] + 1000:
        dist[y][x][(dir + 3) % 4] = dist[y][x][dir] + 1000
        Q.append([y, x, (dir + 3) % 4])
        parent[ (y, x, (dir + 3) % 4) ].clear()
        parent[ (y, x, (dir + 3) % 4) ].append( (y, x, dir) )
    elif dist[y][x][(dir + 3) % 4] == dist[y][x][dir] + 1000:
        parent[ (y, x, (dir + 3) % 4) ].append( (y, x, dir) )


best_sol = min(min(dist[endY][endX][0], dist[endY][endX][1]), min(dist[endY][endX][2], dist[endY][endX][3]))
print(best_sol)

visited = [[0 for j in range(len(grid[0]))] for i in range(len(grid))]

numberOfPaths = 0
for dir in range(4):
    if dist[endY][endX][dir] == best_sol:
        countPaths(endY, endX, dir)

count = 0
for y in range(len(visited)):
    for x in range(len(visited[0])):
        if visited[y][x]:
            count += 1
print(count)