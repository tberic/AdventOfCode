f = open('input.txt', 'r')
line = f.readline().strip()
f.close()

n = len(line)
m = 40

grid = []
grid.append('.'+line+'.')

for i in range(1, m):
    row = '.'
    for j in range(1, n+1):
        if ( grid[i-1][j-1]  == '^' and grid[i-1][j]  == '^' and grid[i-1][j+1]  == '.') or \
            ( grid[i-1][j-1]  == '.' and grid[i-1][j]  == '^' and grid[i-1][j+1]  == '^') or \
            ( grid[i-1][j-1]  == '^' and grid[i-1][j]  == '.' and grid[i-1][j+1]  == '.') or \
            ( grid[i-1][j-1]  == '.' and grid[i-1][j]  == '.' and grid[i-1][j+1]  == '^'):
            row += '^'
        else:
            row += '.'

    row += '.'
    grid.append(row)

#print(grid)
print(len(grid), len(grid[0]))

count = 0
for i in range(m):
    for j in range(n):
        count += grid[i][j+1]=='.'

print(count)