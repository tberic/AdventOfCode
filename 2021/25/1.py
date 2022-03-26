def ispis(a):
    for i in range(len(a)):
        for j in range(len(a[i])):
            print(a[i][j], end='')
        print()

f = open('input.txt', 'r')
grid = [list(line.strip()) for line in f]
f.close()

m = len(grid)
n = len(grid[0])

moves = 1
steps = 0
while moves != 0:
    steps += 1
    grid2 = [['.' for j in range(n)] for i in range(m)]
    moves = 0
    for i in range(m):
        for j in range(n):
            if grid[i][j] == '>' and grid[i][(j+1)%n] == '.':
                grid2[i][(j+1)%n] = '>'
                moves = 1
    for i in range(m):
        for j in range(n):
            if grid2[i][j] == '>':
                grid[i][j] = '>'
                grid[i][(j-1)%n] = '.'

    grid2 = [['.' for j in range(n)] for i in range(m)]
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 'v' and grid[(i+1)%m][j] == '.':
                grid2[(i+1)%m][j] = 'v'
                moves = 1
    for i in range(m):
        for j in range(n):
            if grid2[i][j] == 'v':
                grid[i][j] = 'v'
                grid[(i-1)%m][j] = '.'
    #print('-'*10 + str(steps) + '-'*10)
    #ispis(grid)
                
print(steps)