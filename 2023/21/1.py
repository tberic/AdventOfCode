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

visited = set()
Q = [(startY, startX, 64)]

positions = 0
while Q:
    y, x, steps = Q.pop(0)

    if (y, x, steps) in visited:
        continue

    visited.add( (y, x, steps) )

    if steps == 0:
        positions += 1
        continue

    if y > 0 and grid[y-1][x] != '#':
        Q.append( (y-1, x, steps-1) )
    if y < len(grid)-1 and grid[y+1][x] != '#':
        Q.append( (y+1, x, steps-1) )        
    if x > 0 and grid[y][x-1] != '#':
        Q.append( (y, x-1, steps-1) )
    if x < len(grid[0])-1 and grid[y][x+1] != '#':
        Q.append( (y, x+1, steps-1) )

print(positions)