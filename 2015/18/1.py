def ispis(a):
    for i in range(len(a)):
        for j in range(len(a)):
            print(a[i][j], end='')
        print()
    print()

def neighbors(grid, x, y):
    return (grid[x-1][y-1] == '#') + (grid[x-1][y] == '#') + (grid[x-1][y+1] == '#') + \
            (grid[x][y-1] == '#') + (grid[x][y+1] == '#') + \
            (grid[x+1][y-1] == '#') + (grid[x+1][y] == '#') + (grid[x+1][y+1] == '#')

f = open('input.txt', 'r')
lines = [line for line in f]
n = len(lines)
grid = [['.' for j in range(n+2)] for i in range(n+2)]
for i in range(n):
    for j in range(n):
        grid[i+1][j+1] = lines[i][j]
f.close()

#ispis(grid)

for _ in range(100):
    grid2 = [row[:] for row in grid]
    for i in range(n):
        for j in range(n):
            c = neighbors(grid, i+1, j+1)
            if grid[i+1][j+1] == '#' and c not in [2, 3]:
                grid2[i+1][j+1] = '.'
            if grid[i+1][j+1] == '.' and c == 3:
                grid2[i+1][j+1] = '#'

    grid = [row[:] for row in grid2]
    #ispis(grid)

count = 0
for i in range(n):
    for j in range(n):
        count += grid[i+1][j+1] == '#'
print(count)