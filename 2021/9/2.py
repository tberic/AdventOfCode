f = open('input.txt', 'r')

grid = [[9 for i in range(102)]]
visited = [[0 for i in range(102)] for j in range(102)]

def floodFill(x, y):
    if (visited[x][y]):
        return 0
    if (grid[x][y] == 9):
        return 0

    visited[x][y] = 1

    return floodFill(x-1,y) + floodFill(x+1,y) + floodFill(x,y-1) + floodFill(x,y+1) + 1


for line in f:
    line = line[:-1]
    line = '9' + line + '9'
    a = [int(x) for x in line]
    grid.append(a)

a = [9 for i in range(102)]
grid.append(a)

basins = []

for i in range(1, 101):
    for j in range(1, 101):
        n = floodFill(i,j)
        if (n != 0):
            basins.append(n)

basins.sort(reverse=True)
print(basins[0]*basins[1]*basins[2])

f.close()
