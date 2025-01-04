def outOfBounds(x, y):
    if x < 0 or y < 0:
        return True
    if x >= len(grid):
        return True
    if y >= len(grid[0]):
        return True
    return False

f = open('input.txt')

UP = [-1, 0]
DOWN = [+1, 0]
LEFT = [0, -1]
RIGHT = [0, +1]

grid = [line.strip() for line in f]
visited = [[0 for j in range(len(grid[0]))] for i in range(len(grid))]

X = -1
Y = -1
dir = []
for i, line in enumerate(grid):
    if line.find('^') != -1:
        X = i
        Y = line.find('^')
        dir = UP
        break

x = X
y = Y
print(dir)
while True:
    if outOfBounds(x, y):
        break
    
    if not outOfBounds(x+dir[0], y+dir[1]) and grid[x+dir[0]][y+dir[1]] == '#':
        if dir == UP:
            dir = RIGHT
        elif dir == RIGHT:
            dir = DOWN
        elif dir == DOWN:
            dir = LEFT
        elif dir == LEFT:
            dir = UP

    visited[x][y] = 1

    x += dir[0]
    y += dir[1]

total = 0
for line in visited:
    total += sum(line)
print(total)