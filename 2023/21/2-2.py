from aoc import *

f = open('input.txt', 'r')
grid = [line.strip() for line in f]

# print(grid)

startY, startX = 0, 0
for i, line in enumerate(grid):
    if 'S' in line:
        startY = i
        startX = line.index('S')
        break

# print(startY, startX)
m = len(grid)
n = len(grid[0])

# for yy in range(m):
#     for xx in range(n):

# print(yy, xx, end=' ')

visited = set()
Q = [(startY, startX, 2*131 + 65)] # 26501365

positions = 0
while Q:
    y, x, steps = Q.pop(0)

    if (y, x, steps) in visited:
        continue

    visited.add( (y, x, steps) )

    if steps == 0:
        positions += 1
        continue

    if grid[(y - 1) % m][x % n] != '#':
        Q.append( (y - 1, x, steps-1) )
    if grid[(y + 1) % m][x % n] != '#':
        Q.append( (y + 1, x, steps-1) )        
    if grid[y % m][(x - 1) % n] != '#':
        Q.append( (y, x - 1, steps-1) )
    if grid[y % m][(x + 1) % n] != '#':
        Q.append( (y, x + 1, steps-1) )

print(positions)