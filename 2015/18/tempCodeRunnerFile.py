ispis(grid)

for _ in range(4):
    grid2 = grid.copy()
    print('x'*(n+2))
    for i in range(n):
        print('x', end='')
        for j in range(n):
            c = neighbors(i+1, j+1)
            print(c, end='')
            if grid[i+1][j+1] == '#' and c not in [2, 3]:
                grid2[i+1][j+1] = '.'
            if grid[i+1][j+1] == '.' and c == 3:
                grid2[i+1][j+1] = '#'
        print('x')
    print('x'*(n+2))

    grid = grid2.copy()
    ispis(grid)

