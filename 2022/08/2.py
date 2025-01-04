def look_right(grid, x, y):
    height = grid[x][y]
    nTrees = 0
    for j in range(y+1, len(grid[0])):
        nTrees += 1
        if grid[x][j] >= height:            
            return nTrees
    return nTrees

def look_left(grid, x, y):
    height = grid[x][y]
    nTrees = 0
    for j in range(y-1, -1, -1):
        nTrees += 1
        if grid[x][j] >= height:            
            return nTrees
    return nTrees

def look_up(grid, x, y):
    height = grid[x][y]
    nTrees = 0
    for i in range(x-1, -1, -1):
        nTrees += 1
        if grid[i][y] >= height:
            return nTrees
    return nTrees

def look_down(grid, x, y):
    height = grid[x][y]
    nTrees = 0
    for i in range(x+1, len(grid)):
        nTrees += 1
        if grid[i][y] >= height:
            return nTrees
    return nTrees

def score(grid, x, y):
    return look_right(grid, x, y) * look_left(grid, x, y) * look_up(grid, x, y) * look_down(grid, x, y)

fin = open('input.txt', 'r')

grid = [list(map(int, list(line.strip()))) for line in fin]

maxScore = 0
for x in range(len(grid)):
    for y in range(len(grid[0])):
        curScore = score(grid, x, y)
        if curScore > maxScore:
            maxScore = curScore

print(maxScore)