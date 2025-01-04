def outOfBounds(x, y):
    if x < 0 or y < 0:
        return True
    if x >= len(grid):
        return True
    if y >= len(grid[0]):
        return True
    return False

def DFS(x, y):
    visited = [[0 for j in range(len(grid[0]))] for i in range(len(grid))]
    S = [(x, y)]
    score = 0
    
    while S:
        x, y = S.pop()
        if outOfBounds(x, y):
            continue
        if visited[x][y]:
            continue

        visited[x][y] = 1

        if grid[x][y] == 9:
            score += 1
            continue

        for dir in DIRS:
            xx = x + dir[0]
            yy = y + dir[1]
            if not outOfBounds(xx, yy) and grid[xx][yy] - grid[x][y] == 1:
                S.append((xx, yy))
        
    return score

DIRS = [
    [-1, 0],
    [+1, 0],
    [0, -1],
    [0, +1]
]

f = open('input.txt')

grid = [list(map(int, list(line.strip()))) for line in f]

trailheads = []
for x in range(len(grid)):
    for y in range(len(grid[0])):
        if grid[x][y] == 0:
            trailheads.append([x, y])

total = 0
for trailhead in trailheads:
    total += DFS(trailhead[0], trailhead[1])
print(total)