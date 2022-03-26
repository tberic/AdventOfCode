def sumNeighbors(x, y):
    global grid
    return grid[x-1][y-1] + grid[x][y-1] + grid[x+1][y-1] + \
            grid[x-1][y] +               + grid[x+1][y] + \
            grid[x-1][y+1] + grid[x][y+1] + grid[x+1][y+1]

n = 347991

N = 20
grid = [[0 for j in range(2*N+1)] for i in range(2*N+1)]

grid[0 + N][0 + N] = 1
k = 3
x, y = (0, 0)
done = 0
while not done:
    y += 1
    grid[x + N][y + N] = sumNeighbors(x + N, y + N)
    if grid[x + N][y + N] > n:
        print(grid[x + N][y + N])
        done = 1
        break

    if done:
        break

    for i in range(k-2):
        x -= 1
        grid[x + N][y + N] = sumNeighbors(x + N, y + N)
        if grid[x + N][y + N] > n:
            print(grid[x + N][y + N])
            done = 1
            break

    if done:
        break

    for i in range(k-1):
        y -= 1
        grid[x + N][y + N] = sumNeighbors(x + N, y + N)
        if grid[x + N][y + N] > n:
            print(grid[x + N][y + N])
            done = 1
            break

    if done:
        break

    for i in range(k-1):
        x += 1
        grid[x + N][y + N] = sumNeighbors(x + N, y + N)
        if grid[x + N][y + N] > n:
            print(grid[x + N][y + N])
            done = 1
            break

    if done:
        break

    for i in range(k-1):
        y += 1
        grid[x + N][y + N] = sumNeighbors(x + N, y + N)
        if grid[x + N][y + N] > n:
            print(grid[x + N][y + N])
            done = 1
            break

    k += 2

print(x, y)
#print(grid)