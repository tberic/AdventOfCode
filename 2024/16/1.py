import heapq

DIRS = [
    [0, +1], 
    [-1, 0],
    [0, -1], 
    [+1, 0]
]

DIR_MASK = [1, 2, 4, 8]

f = open('input.txt')

grid = [line.strip() for line in f]

for y in range(len(grid)):
    for x in range(len(grid[0])):
        if grid[y][x] == 'S':
            startY, startX = y, x
        if grid[y][x] == 'E':
            endY, endX = y, x

# Dijkstra's algorithm
sol = 0
PQ = []
heapq.heappush(PQ, [0, startY, startX, 0])

visited = [[0 for j in range(len(grid[0]))] for i in range(len(grid))]

while PQ:
    score, y, x, dir = heapq.heappop(PQ)
    if y == endY and x == endX:
        sol = score
        break
    if visited[x][y] & DIR_MASK[dir]:
        continue

    visited[x][y] |= DIR_MASK[dir]

    if score % 1000 == 0:
        print(score)

    if grid[y][x] == '#':
        continue

    heapq.heappush(PQ, [score+1, y+DIRS[dir][0], x+DIRS[dir][1], dir])
    heapq.heappush(PQ, [score+1000, y, x, (dir + 1) % 4])
    heapq.heappush(PQ, [score+1000, y, x, (dir + 3) % 4])

print(sol)