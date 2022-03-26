def parse(i, x, y):
    global line, minx, maxx, miny, maxy

    if i >= len(line):
        return False

    if line[i] == '$':
        return False
    if line[i] == ')':
        return i+1, ')'

    while i < len(line):

        while line[i] not in ['$', ')'] and line[i] in "NSWE":
            if line[i] == 'N':
                y -= 1
            elif line[i] == 'S':
                y += 1
            elif line[i] == 'W':
                x -= 1
            elif line[i] == 'E':
                x += 1

            if x < minx:
                minx = x
            if x > maxx:
                maxx = x
            if y < miny:
                miny = y
            if y > maxy:
                maxy = y

            i += 1

        if line[i] == '$':
            return False        
        if line[i] == ')':
            return i+1, ')'
        if line[i] == '|':
            return i+1, '|'

        if line[i] == '(':
            r = parse(i+1, x, y)
            j, c = r
            while c != ')':
                r = parse(j, x, y)
                if not r:
                    break
                j, c = r    

        i = j


def generateRooms(i, x, y):
    global line, grid

    if i >= len(line):
        return False

    if line[i] == '$':
        return False
    if line[i] == ')':
        return i+1, ')'

    while i < len(line):

        while line[i] not in ['$', ')'] and line[i] in "NSWE":
            grid[y][x] = '.'
            if line[i] == 'N':
                grid[y-1][x] = '-'
                y -= 2                
            elif line[i] == 'S':
                grid[y+1][x] = '-'
                y += 2
            elif line[i] == 'W':
                grid[y][x-1] = '|'
                x -= 2
            elif line[i] == 'E':
                grid[y][x+1] = '|'
                x += 2

            i += 1

        grid[y][x] = '.'

        if line[i] == '$':
            return False        
        if line[i] == ')':
            return i+1, ')'
        if line[i] == '|':
            return i+1, '|'

        if line[i] == '(':
            r = generateRooms(i+1, x, y)
            j, c = r
            while c != ')':
                r = generateRooms(j, x, y)
                if not r:
                    break
                j, c = r    

        i = j



f = open('input.txt', 'r')
line = f.readline().strip()
f.close()

# first let's see the farthest we go in each direction

minx, maxx, miny, maxy = 0, 0, 0, 0
parse(1, 0, 0) # pos, x, y
print(minx, maxx, miny, maxy)

# now we can construct the grid

grid = [ ['#'] + list('?'*( 2*(maxx-minx) + 1 )) + ['#'] for i in range( (maxy-miny)*2+1 ) ]
grid.append( list('#' * len(grid[0])) )
grid.insert(0, list('#' * len(grid[0])) )


posx = 1 - 2*minx
posy = 1 - 2*miny
generateRooms(1, posx, posy)
grid[posy][posx] = 'X'

# replace ? with # everywhere

for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j] == '?':
            grid[i][j] = '#'

g = open('maze.txt', 'w')
for i in range(len(grid)):
    print("".join(grid[i]), file=g)
g.close()

# now find the room farthest away from origin, we will use DFS to traverse all the rooms
visited = [ [0 for j in range(len(grid[i]))] for i in range(len(grid))]
S = []
S.append( (0, posy, posx) )

while S:
    d, y, x = S.pop()

    visited[y][x] = d

    if grid[y-1][x] == '-' and not visited[y-2][x]:
        S.append( (d+1, y-2, x) )
    if grid[y+1][x] == '-' and not visited[y+2][x]:
        S.append( (d+1, y+2, x) )
    if grid[y][x-1] == '|' and not visited[y][x-2]:
        S.append( (d+1, y, x-2) )
    if grid[y][x+1] == '|' and not visited[y][x+2]:
        S.append( (d+1, y, x+2) )

maxSteps = 0
count1000 = 0
for i in range(len(visited)):
    m = max(visited[i])
    if m > maxSteps:
        maxSteps = m
    for j in range(len(visited[i])):
        if visited[i][j] >= 1000:
            count1000 += 1

print(maxSteps)
print(count1000)