f = open('input.txt')

def prettyPrint(grid):
    for y in range(M):
        for x in range(N):
            print(grid[y][x], end='')
        print()
    print()


UP = [-1, 0]
DOWN = [+1, 0]
LEFT = [0, -1]
RIGHT = [0, +1]
DIRS = {'<': LEFT, '>': RIGHT, '^': UP, 'v': DOWN}

WALL = '#'
BOX = 'O'
EMPTY = '.'

moves = []
grid = []

readMoves = False
for line in f:
    if line == '\n':
        readMoves = True
        continue

    if readMoves:
        moves += list(line.strip())
    else:
        grid.append( list(line.strip()) )

M = len(grid)
N = len(grid[0])

for y in range(M):
    for x in range(N):
        if grid[y][x] == '@':
            y0, x0 = y, x
grid[y0][x0] = '.'

y, x = y0, x0
for move in moves:
    dir = DIRS[move]
    
    yy = y + dir[0]
    xx = x + dir[1]
    if grid[yy][xx] == WALL:
        continue
    if grid[yy][xx] == EMPTY:
        y, x = yy, xx
        continue
    if grid[yy][xx] == BOX:
        yyy, xxx = yy, xx
        while grid[yyy][xxx] == BOX:
            yyy += dir[0]
            xxx += dir[1]
        if grid[yyy][xxx] == EMPTY:
            while yyy != yy or xxx != xx:
                grid[yyy][xxx] = BOX
                yyy -= dir[0]
                xxx -= dir[1]
            grid[yy][xx] = EMPTY
            y, x = yy, xx
        else:
            continue
    else:
        print('ERROR: unknown character in the grid!')

# prettyPrint(grid)

total = 0
for y in range(M):
    for x in range(N):
        if grid[y][x] == BOX:
            total += 100*y + x
            
print(total)