import sys

UP = (-1, 0)
DOWN = (+1, 0)
LEFT = (0, -1)
RIGHT = (0, +1)

def hash(dir):
    if dir == UP:
        return 1
    if dir == DOWN:
        return 2
    if dir == LEFT:
        return 4
    if dir == RIGHT:
        return 8
    return 0

def follow(y, x, dir):
    if y < 0 or y >= len(grid):
        return
    if x < 0 or x >= len(grid[0]):
        return
    if visited[y][x] & hash(dir):
        return
    
    visited[y][x] |= hash(dir)

    if grid[y][x] == '.':
        follow(y + dir[0], x + dir[1], dir)
    elif grid[y][x] == '/':
        if dir == UP:
            follow(y, x + 1, RIGHT)
        elif dir == DOWN:
            follow(y, x - 1, LEFT)
        elif dir == RIGHT:
            follow(y - 1, x, UP)
        elif dir == LEFT:
            follow(y + 1, x, DOWN)
    elif grid[y][x] == '\\':
        if dir == UP:
            follow(y, x - 1, LEFT)
        elif dir == DOWN:
            follow(y, x + 1, RIGHT)
        elif dir == RIGHT:
            follow(y + 1, x, DOWN)
        elif dir == LEFT:
            follow(y - 1, x, UP)
    elif grid[y][x] == '-':
        if dir == LEFT or dir == RIGHT:
            follow(y + dir[0], x + dir[1], dir)
        else:
            follow(y, x - 1, LEFT)
            follow(y, x + 1, RIGHT)
    elif grid[y][x] == '|':
        if dir == UP or dir == DOWN:
            follow(y + dir[0], x + dir[1], dir)
        else:
            follow(y - 1, x, UP)
            follow(y + 1, x, DOWN)
    

f = open('input.txt', 'r')

grid = [line.strip() for line in f]
m = len(grid)
n = len(grid[0])

sys.setrecursionlimit(100000)

# check all the possibilities
maxEnergized = 0
possibilities = []
possibilities.append([(0, 0), RIGHT])
possibilities.append([(0, 0), DOWN])
possibilities.append([(0, n-1), LEFT])
possibilities.append([(0, n-1), DOWN])
possibilities.append([(m-1, n-1), LEFT])
possibilities.append([(m-1, n-1), UP])
possibilities.append([(m-1, 0), RIGHT])
possibilities.append([(m-1, 0), UP])
for x in range(1, n-1):
    possibilities.append([(0, x), DOWN])
    possibilities.append([(m-1, x), UP])
for y in range(1, m-1):
    possibilities.append([(y, 0), RIGHT])
    possibilities.append([(y, n-1), LEFT])

for start in possibilities:
    visited = [[0 for j in range(len(grid[0]))] for i in range(len(grid))]
    follow(start[0][0], start[0][1], start[1])
    energized = 0
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if visited[y][x]:
                energized += 1
    if energized > maxEnergized:
        maxEnergized = energized

print(maxEnergized)
