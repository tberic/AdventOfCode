def trypush(y1, x1, y2, x2, dir):
    if grid[y1+dir[0]][x1+dir[1]] == WALL or grid[y2+dir[0]][x2+dir[1]] == WALL:
        return False

    if grid[y1+dir[0]][x1+dir[1]] == EMPTY and grid[y2+dir[0]][x2+dir[1]] == EMPTY:
        return True

    grid[y1][x1] = '.'
    grid[y2][x2] = '.'

    push1 = True
    push2 = True
    if grid[y1+dir[0]][x1+dir[1]] == '[':
        push1 = trypush( y1+dir[0], x1+dir[1], y1+dir[0], x1+dir[1]+1, dir )
    elif grid[y1+dir[0]][x1+dir[1]] == ']':
        push1 = trypush( y1+dir[0], x1+dir[1]-1, y1+dir[0], x1+dir[1], dir )

    if grid[y2+dir[0]][x2+dir[1]] == '[':
        push2 = trypush( y2+dir[0], x2+dir[1], y2+dir[0], x2+dir[1]+1, dir )
    elif grid[y2+dir[0]][x2+dir[1]] == ']':
        push2 = trypush( y2+dir[0], x2+dir[1]-1, y2+dir[0], x2+dir[1], dir )

    grid[y1][x1] = '['
    grid[y2][x2] = ']'

    return push1 and push2


def push(y1, x1, y2, x2, dir):
    if grid[y1+dir[0]][x1+dir[1]] == WALL or grid[y2+dir[0]][x2+dir[1]] == WALL:
        return False

    grid[y1][x1] = EMPTY
    grid[y2][x2] = EMPTY

    push1 = True
    push2 = True
    if grid[y1+dir[0]][x1+dir[1]] == '[':
        push1 = push( y1+dir[0], x1+dir[1], y1+dir[0], x1+dir[1]+1, dir )
    elif grid[y1+dir[0]][x1+dir[1]] == ']':
        push1 = push( y1+dir[0], x1+dir[1]-1, y1+dir[0], x1+dir[1], dir )

    if grid[y2+dir[0]][x2+dir[1]] == '[':
        push2 = push( y2+dir[0], x2+dir[1], y2+dir[0], x2+dir[1]+1, dir )
    elif grid[y2+dir[0]][x2+dir[1]] == ']':
        push2 = push( y2+dir[0], x2+dir[1]-1, y2+dir[0], x2+dir[1], dir )

    if not push1 or not push2:
        grid[y1][x1] = '['
        grid[y2][x2] = ']'
        return False

    if grid[y1+dir[0]][x1+dir[1]] == EMPTY and grid[y2+dir[0]][x2+dir[1]] == EMPTY:
        grid[y1+dir[0]][x1+dir[1]] = '['
        grid[y2+dir[0]][x2+dir[1]] = ']'
        return True
    
    return False


def prettyPrint(grid, y0, x0, dir=None):
    for y in range(M):
        for x in range(N):
            if y == y0 and x == x0:
                if dir:
                    print(dir, end='')    
                else:
                    print('@', end='')
            else:
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
WIDEBOX = '[]'
EMPTY = '.'

f = open('input.txt')

moves = []
smallGrid = []
grid = []

readMoves = False
for line in f:
    if line == '\n':
        readMoves = True
        continue

    if readMoves:
        moves += list(line.strip())
    else:
        smallGrid.append( list(line.strip()) )

for y in range(len(smallGrid)):
    grid.append([])
    for x in range(len(smallGrid[0])):
        if smallGrid[y][x] == '.':
            grid[-1] += '..'
        if smallGrid[y][x] == '@':
            grid[-1] += '@.'
        if smallGrid[y][x] == 'O':
            grid[-1] += '[]'
        if smallGrid[y][x] == '#':
            grid[-1] += '##'

M = len(grid)
N = len(grid[0])
# prettyPrint(grid)

for y in range(M):
    for x in range(N):
        if grid[y][x] == '@':
            y0, x0 = y, x
grid[y0][x0] = '.'

y, x = y0, x0
for move in moves:
    # print(move, y, x)
    # prettyPrint(grid, y, x, move)
    # input()
    dir = DIRS[move]
    
    yy = y + dir[0]
    xx = x + dir[1]
    if grid[yy][xx] == WALL:
        continue
    if grid[yy][xx] == EMPTY:
        y, x = yy, xx
        continue
    if grid[yy][xx] in WIDEBOX:
        if grid[yy][xx] == '[':
            y1, x1 = yy, xx
            y2, x2 = yy, xx+1
        elif grid[yy][xx] == ']':
            y1, x1 = yy, xx-1
            y2, x2 = yy, xx
        if trypush(y1, x1, y2, x2, dir):
            push(y1, x1, y2, x2, dir)
            y, x = yy, xx
    else:
        print('ERROR: unknown character in the grid!')

prettyPrint(grid, y, x)

total = 0
for y in range(M):
    for x in range(N):
        if grid[y][x] == '[':
            total += 100*y + x
            
print(total)