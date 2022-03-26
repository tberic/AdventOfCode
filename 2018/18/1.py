def valid(x, y):
    global grid
    if x < 0 or y < 0:
        return False
    if x >= len(grid) or y >= len(grid):
        return False
    return True

def around(x, y, c):
    global grid, dirs
    count = 0
    for a,b in dirs:
        if valid(x+a, y+b) and grid[x+a][y+b] == c:
            count += 1
    return count

dirs = [(-1, -1), (-1, 0), (-1, +1), (0, -1), (0, +1), (+1, -1), (+1, 0), (+1, +1)]

f = open('input.txt', 'r')
grid = [list(line.strip()) for line in f]
f.close()

for _ in range(10):
    grid2 = [row[:] for row in grid]

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == '.' and around(i, j, '|') >= 3:
                grid2[i][j] = '|'            
            elif grid[i][j] == '|' and around(i, j, '#') >= 3:
                grid2[i][j] = '#'
            elif grid[i][j] == '#' and (around(i, j, '|') == 0 or around(i, j, '#') == 0):
                grid2[i][j] = '.'

    grid = [row[:] for row in grid2]
    for i in range(len(grid)):
        print("".join(grid[i]))    
    print()


wooded = 0
lumberyard = 0
for i in range(len(grid)):
    for j in range(len(grid[i])):
        if grid[i][j] == '|':
            wooded += 1
        elif grid[i][j] == '#':
            lumberyard += 1
print(wooded * lumberyard)