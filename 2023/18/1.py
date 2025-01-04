MAXN = 500
OFFSET = 200

import sys
from aoc import *

def floodFill(y, x, target):
    stack = [(y, x)]
    while stack:
        y, x = stack.pop()

        if y < 0 or y >= len(grid):
            continue
        if x < 0 or x >= len(grid[0]):
            continue
        if grid[y][x]:
            continue
        grid[y][x] = target

        stack.append((y-1, x))
        stack.append((y+1, x))
        stack.append((y, x-1))
        stack.append((y, x+1))



f = open('input.txt', 'r')

lines = [line.strip() for line in f]

dirs = {'R': RIGHT, 'L': LEFT, 'D': DOWN, 'U': UP}

grid = [[0 for j in range(MAXN)] for i in range(MAXN)]
y, x = OFFSET, OFFSET
grid[y][x] = 1
maxX = maxY = -10 ** 10
minX = minY = 10 ** 10
# y, x = 0, 0
for line in lines:
    dirIn, n, _ = line.split(' ')
    n = int(n)

    dir = dirs[dirIn]

    for i in range(n):
        y += dir[0]
        x += dir[1]
        grid[y][x] = 1

    # y += n * dir[0]
    # x += n * dir[1]

    if x > maxX:
        maxX = x
    if x < minX:
        minX = x        
    if y > maxY:
        maxY = y
    if y < minY:
        minY = y                

print(minY, minX, maxY, maxX)

sys.setrecursionlimit(1000000)
y, x = OFFSET+20, OFFSET+20
print(grid[y][x])
floodFill(y, x, 2)

cells = 0
for y in range(len(grid)):
    for x in range(len(grid[0])):
        if grid[y][x] in [0, 1]:
            cells += 1
print(cells)

# for y in range(minY, maxY+1):
#     for x in range(minX, maxX+1):
#         print(grid[y][x], end='')
#     print()
