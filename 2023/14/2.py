def printArray(A):
    for row in A:
        print("".join(row))
    print()

def rot(A):
    m = len(A)
    n = len(A[0])
    B = [[0 for j in range(n)] for i in range(m)]
    
    for i in range(n):
        for j in range(m):
            B[i][j] = A[m-j-1][i]
    
    return B

def rollNorth(grid):
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if grid[y][x] == 'O':
                yy = y
                while yy > 0:
                    yy -= 1
                    if grid[yy][x] in ['#', 'O']:
                        yy += 1
                        break

                grid[y][x] = '.'
                grid[yy][x] = 'O'
    return grid

def rollSouth(grid):
    return grid

def rollWest(grid):
    return grid

def rollEast(grid):
    return grid

f = open('input.txt', 'r')

grid = [list(line.strip()) for line in f]

seen = {}

for i in range(1000000000): #1000000000
    grid = rollNorth(grid)
    grid = rot(grid)
    grid = rollNorth(grid)
    grid = rot(grid)
    grid = rollNorth(grid)
    grid = rot(grid)
    grid = rollNorth(grid)
    grid = rot(grid)
    
    gridString = ["".join(row) for row in grid]
    gridString = "".join(gridString)
    
    if gridString in seen:
        print(i, seen[gridString])
        break
    else:
        seen[gridString] = i

# printArray(grid)

period = i-seen[gridString]
iterations = (1000000000 - i) % period

for i in range(iterations-1):
    grid = rollNorth(grid)
    grid = rot(grid)
    grid = rollNorth(grid)
    grid = rot(grid)
    grid = rollNorth(grid)
    grid = rot(grid)
    grid = rollNorth(grid)
    grid = rot(grid)

sum = 0
n = len(grid)
for y in range(len(grid)):
    for x in range(len(grid[0])):
        if grid[y][x] == 'O':
            sum += n-y

print(sum)