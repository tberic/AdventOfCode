def modify(x):
    if x <= 9:
        return x
    else:
        return x%9

f = open('input.txt', 'r')

grid_small = []
for line in f:
    a = [int(x) for x in line.strip()]
    grid_small.append(a)
n_small = len(grid_small)
n = n_small*5

grid = [[0 for i in range(n)] for j in range(n)]
#create extended grid
for i in range(5):
    for j in range(5):
        for x in range(n_small):
            for y in range(n_small):
                grid[ x + i*n_small ][ y + j*n_small ] = modify(grid_small[x][y] + (i+j))
       

g = open('input_large.txt', 'w')

for i in range(n):
    for j in range(n):
        print(grid[i][j], end='', file=g)
    print(file=g)
#print(n)


f.close()
g.close()