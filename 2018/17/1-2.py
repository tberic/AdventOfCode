def solid(c):
    return c in ['#', '~']

def sand(c):
    return c in ['.', '|']

def drip(y, x):
    global grid, dontVisit
    
    count = 0
    while y+1 < len(grid) and sand(grid[y+1][x]):
        y += 1
        if grid[y][x] == '.':
            grid[y][x] = '|'
            count += 1
    if y == len(grid)-1:
        return count
    
    a = x
    while a > 0 and sand(grid[y][a-1]) and solid(grid[y+1][a]):
        if grid[y][a] == '.':
            grid[y][a] = '|'
            count += 1
        a -= 1
    grid[y][a] = '|'
    # if a == 0: #left edge, we don't count it
    #     pass
    

    b = x
    while b < len(grid[y]) and sand(grid[y][b+1]) and solid(grid[y+1][b]):
        if grid[y][b] == '.':
            grid[y][b] = '|'
            count += 1
        b += 1
    grid[y][b] = '|'
    # if b == len(grid[y])-1:
    #     pass

    # if it just drips down off the edge of the grid, we won't go there the next time

    s1 = 0
    if not solid(grid[y+1][a]) and not dontVisit[y][a]:
        s1 = drip(y, a)
        if s1 == 0:
            dontVisit[y][a] = 1
    count += s1

    s2 = 0
    if not solid(grid[y+1][b]) and not dontVisit[y][b]:
        s2 = drip(y, b)    
        if s2 == 0:
            dontVisit[y][b] = 1
    count += s2

    if a > 0 and grid[y][a-1] == '#' and \
        b < len(grid[y])-1 and grid[y][b+1] == '#' and \
        solid(grid[y+1][a]) and solid(grid[y+1][b]): # we will turn this segment into still water
        for i in range(a, b+1):
            grid[y][i] = '~'
            count += b-a+1

    return count


f = open('output.txt', 'r')
grid = [['.']+list(line.strip())+['.'] for line in f]
offsetx, offsety = list(map(int, ("".join(grid[-1][1:-1])).split() ))
grid.pop()
f.close()

xSource = 500-offsetx+1
dontVisit = [[0 for j in range(len(grid[i]))] for i in range(len(grid))]

grid[0][xSource] = '|'

count = 1
nCells = -1
while count:
    nCells += count
    count = drip(0, xSource)
    #print(count)
    

g = open('water.txt', 'w')
for row in grid:
    print("".join(row), file=g)
g.close()


countRunning = 0
countStill = 0
for i in range(len(grid)):
    for j in range(len(grid[i])):
        if grid[i][j] == '|':
            countRunning += 1
        elif grid[i][j] == '~':
            countStill += 1

print(countRunning + countStill)
print(countStill)