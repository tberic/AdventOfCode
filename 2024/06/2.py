def outOfBounds(x, y):
    if x < 0 or y < 0:
        return True
    if x >= len(grid):
        return True
    if y >= len(grid[0]):
        return True
    return False

def dirName(dir):
    if dir == UP:
        return "UP"
    if dir == DOWN:
        return "DOWN"
    if dir == LEFT:
        return "LEFT"
    if dir == RIGHT:
        return "RIGHT"
    return "UNKNOWN"


f = open('input.txt')

UP = [-1, 0]
DOWN = [+1, 0]
LEFT = [0, -1]
RIGHT = [0, +1]

dirs = {"UP": 1, "DOWN": 2, "LEFT": 4, "RIGHT": 8}

grid = [list(line.strip()) for line in f]

X = -1
Y = -1
dir = []
for x in range(len(grid)):
    for y in range(len(grid[0])):
        if grid[x][y] == '^':
            X = x
            Y = y
            break


originalPath = [[0 for j in range(len(grid[0]))] for i in range(len(grid))]
x = X
y = Y
dir = UP
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

    originalPath[x][y] = 1

    x += dir[0]
    y += dir[1]


loops = 0
for i in range(len(grid)):
    for j in range(len(grid[0])):
        if originalPath[i][j] == 0:
            continue
        if grid[i][j] == '^' or grid[i][j] == '#':
            continue

        grid[i][j] = '#'

        x = X
        y = Y
        dir = UP
        visited = [[0 for j in range(len(grid[0]))] for i in range(len(grid))]
        Loop = False
        while True:
            if outOfBounds(x, y):
                break
            
            if visited[x][y] & dirs[dirName(dir)]:
                Loop = True
                break

            visited[x][y] |= dirs[dirName(dir)]

            while not outOfBounds(x+dir[0], y+dir[1]) and grid[x+dir[0]][y+dir[1]] == '#':
                if dir == UP:
                    dir = RIGHT
                elif dir == RIGHT:
                    dir = DOWN
                elif dir == DOWN:
                    dir = LEFT
                elif dir == LEFT:
                    dir = UP
                # visited[x][y] |= dirs[dirName(dir)]

            x += dir[0]
            y += dir[1]

        if Loop:
            loops += 1
            # print(i, j)

        grid[i][j] = '.'

print(loops)