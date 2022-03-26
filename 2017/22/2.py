N = 3000
grid = [ [0 for j in range(N)] for i in range(N) ]
offsetx = N//2
offsety = N//2

f = open('input.txt', 'r')
lines = [line.strip() for line in f]
f.close()

middle = len(lines)//2
for i, line in enumerate(lines):
    for j, c in enumerate(line):
        if c == '#':
            grid[i-middle+offsetx][j-middle+offsety] = 2
        else:
            grid[i-middle+offsetx][j-middle+offsety] = 0

state = 0
directions = [(-1, 0), (0, +1), (+1, 0), (0, -1)]
dir = 0
(x, y) = (0, 0)

minx, miny, maxx, maxy = (-middle, -middle, +middle, +middle)

count = 0
for _ in range(10000000):

    # print()
    # for i in range(minx, maxx+1):
    #     for j in range(miny, maxy+1):
    #         print(grid[i+offsetx][j+offsety], end='')
    #     print()
    # print()

    if grid[x+offsetx][y+offsety] == 0:
        dir = (dir-1)%4
        grid[x+offsetx][y+offsety] = 1
    elif grid[x+offsetx][y+offsety] == 1:
        count += 1
        grid[x+offsetx][y+offsety] = 2
    elif grid[x+offsetx][y+offsety] == 2:        
        dir = (dir+1)%4
        grid[x+offsetx][y+offsety] = 3
    elif grid[x+offsetx][y+offsety] == 3:
        dir = (dir+2)%4
        grid[x+offsetx][y+offsety] = 0

    minx = min(minx, x)
    maxx = max(maxx, x)
    miny = min(miny, y)
    maxy = max(maxy, y)

    x, y = x+directions[dir][0], y+directions[dir][1]

print(count)
print(minx, miny, maxx, maxy)