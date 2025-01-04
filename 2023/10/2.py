# This algorithm doesn't work properly. For the official test input, 
# ten grid points were left unclassified. So I guessed the solution
# in the range of [output, output+10]

BORDER = 1
INSIDE = 2
OUTSIDE = 3

UP = [-1, 0]
DOWN = [+1, 0]
RIGHT = [0, +1]
LEFT = [0, -1]

import sys
import numpy as np
from numpy import array
import matplotlib.pyplot as plt

def printArray(a):
    for y in range(len(a)):
        for x in range(len(a[0])):
            print(a[y][x], end='')
        print()
    print()

def east(y, x):
    return grid[y][x] == '-' or grid[y][x] == 'L' or grid[y][x] == 'F'

def west(y, x):
    return grid[y][x] == '-' or grid[y][x] == 'J' or grid[y][x] == '7'

def south(y, x):
    return grid[y][x] == '|' or grid[y][x] == '7' or grid[y][x] == 'F'

def north(y, x):
    return grid[y][x] == '|' or grid[y][x] == 'L' or grid[y][x] == 'J'

def convertStart(y, x):
    if south(y-1, x) and north(y+1, x):
        return '|'
    if east(y, x-1) and west(y, x+1):
        return '-'
    if south(y-1, x) and west(y, x+1):
        return 'L'
    if south(y-1, x) and east(y, x-1):
        return 'J'
    if north(y+1, x) and east(y, x-1):
        return '7'
    if north(y+1, x) and west(y, x+1):
        return 'F'

def floodFill(a, y, x, target):
    if x < 0 or x >= len(a[0]) or y < 0 or y >= len(a):
        return 0
    
    if a[y][x] and a[y][x] != 1 and a[y][x] != target:
        print('ERROR')
    
    if a[y][x]:
        return 0
    
    a[y][x] = target
    floodFill(a, y-1, x, target)
    floodFill(a, y+1, x, target)
    floodFill(a, y, x-1, target)
    floodFill(a, y, x+1, target)

def FLOOD_FILL(a, target):
    for y in range(len(a)):
        for x in range(len(a[0])):
            if a[y][x] == target:
                a[y][x] = 0
                floodFill(a, y, x, target)

def findLoop(startY, startX, findInside = False):
    y, x = startY, startX

    if grid[y][x] == '|':
        dir = UP
        inside = RIGHT
    if grid[y][x] == '-':
        dir = RIGHT
        inside = DOWN
    if grid[y][x] == 'F':
        dir = RIGHT
        inside = DOWN
    if grid[y][x] == '7':
        dir = DOWN
        inside = LEFT
    if grid[y][x] == 'J':
        dir = UP
        inside = RIGHT
    if grid[y][x] == 'L':
        dir = UP
        inside = RIGHT

    while True:
        if not findInside:
            loopGrid[y][x] = BORDER

        if findInside and loopGrid[y + inside[0]][x + inside[1]] != BORDER:
            loopGrid[y + inside[0]][x + inside[1]] = INSIDE

        if findInside and loopGrid[y - inside[0]][x - inside[1]] != BORDER:
            loopGrid[y - inside[0]][x - inside[1]] = OUTSIDE

        y = y + dir[0]
        x = x + dir[1]

        if y == startY and x == startX:
            break

        if grid[y][x] == '|':
            pass

        if grid[y][x] == '-':
            pass

        if grid[y][x] == 'L':
            if dir[0]:
                dir = RIGHT
                inside = DOWN
            else:
                dir = UP
                inside = RIGHT

        if grid[y][x] == 'J':
            if dir[0]:
                dir = LEFT
                inside = UP
            else:
                dir = UP
                inside = RIGHT

        if grid[y][x] == '7':
            if dir[0]:
                dir = LEFT
                inside = UP
            else:
                dir = DOWN
                inside = LEFT

        if grid[y][x] == 'F':
            if dir[0]:
                dir = RIGHT
                inside = DOWN
            else:
                dir = DOWN
                inside = LEFT


f = open('input.txt', 'r')

grid = [line.strip() for line in f]

for i in range(len(grid)):
    grid[i] = '..' + grid[i] + '..'
grid.append( '.' * len(grid[0]) )
grid.append( '.' * len(grid[0]) )
grid = ['.' * len(grid[0])] + grid
grid = ['.' * len(grid[0])] + grid

loopGrid = [[0] * len(line) for line in grid]

for y in range(len(grid)):
    for x in range(len(grid[0])):
        if (grid[y][x] == 'S'):
            posX = x
            posY = y

grid[posY] = grid[posY].replace('S', convertStart(posY, posX))
# print(convertStart(posY, posX))

# IDEA: walk along the loop "clockwise" starting from somewhere on the leftmost edge
# everything to the "left" of the loop is outside, everything on the "right" is inside
# keep track of what's inside

findLoop(posY, posX)
# printArray(loopGrid)

leftX = len(loopGrid[0])
leftY = len(loopGrid)
for y in range(len(loopGrid)):
    for x in range(len(loopGrid[0])):
        if grid[y][x] == '|' and loopGrid[y][x] == BORDER and x < leftX:
            leftX = x
            leftY = y

findLoop(leftY, leftX, findInside=True)
# printArray(loopGrid)

# nArray = array(loopGrid)
# plt.imshow(nArray, cmap='gray')
# plt.show()

sys.setrecursionlimit(10000)

FLOOD_FILL(loopGrid, INSIDE)
FLOOD_FILL(loopGrid, OUTSIDE)

# printArray(loopGrid)

nArray = array(loopGrid)
plt.imshow(nArray, cmap='gray')
plt.show()

# def convert(x):
#     if x == 0:
#         return '.'
#     if x == 2:
#         return 'I'
#     return '*'

# loopGrid = loopGrid[2:-2]
# for y in range(len(loopGrid)):
#     for x in range(len(loopGrid[0])):
#         print(convert(loopGrid[y][x]), end='')
#     print()

for y in range(len(loopGrid)):
    for x in range(len(loopGrid[0])):
        if not loopGrid[y][x]:
            print(y, x)

count = 0
for y in range(len(loopGrid)):
    for x in range(len(loopGrid[0])):
        if loopGrid[y][x] == INSIDE:
            count += 1
print(count)