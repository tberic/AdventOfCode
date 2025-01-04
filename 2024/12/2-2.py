from copy import deepcopy

import sys
sys.setrecursionlimit(1000000)

def outOfBounds(x, y):
    return grid[x][y] == '.'

def outOfBoundsXY(x, y):
    if x < 0 or y < 0:
        return True
    if x >= len(grid) or y >= len(grid[0]):
        return True
    return False

def flood_fill_area(x, y, crop, id):
    if outOfBounds(x, y):
        return 0
    if grid[x][y] != crop:
        return 0
    if visited[x][y] & AREA_MASK:
        return 0
    
    visited[x][y] |= AREA_MASK
    regions[x][y] = id
    
    return 1 + flood_fill_area(x-1, y, crop, id) + flood_fill_area(x+1, y, crop, id) \
        + flood_fill_area(x, y-1, crop, id) + flood_fill_area(x, y+1, crop, id)

def calculate_outside_perimeter(xx, yy, region):
    dir = 1
    sides = 0
    while True:
        if visited[xx][yy] & PERIMETER_OUT_MASKS[dir]:
            break
        
        visited[xx][yy] |= PERIMETER_OUT_MASKS[dir]
        while regions[xx + DIRS[dir][0]][yy + DIRS[dir][1]] == region and regions[xx+DIRS_OUT[dir][0]][yy+DIRS_OUT[dir][1]] != region:
            visited[xx][yy] |= PERIMETER_OUT_MASKS[dir]
            xx += DIRS[dir][0]
            yy += DIRS[dir][1]

        sides += 1

        if regions[xx+DIRS_OUT[dir][0]][yy+DIRS_OUT[dir][1]] == region:
            dir = (dir + 3) % 4
            xx += DIRS[dir][0]
            yy += DIRS[dir][1]
        elif regions[xx+DIRS[dir][0]+DIRS_OUT[dir][0]][yy+DIRS[dir][1]+DIRS_OUT[dir][1]] == region:
            xx += DIRS[dir][0]+DIRS_OUT[dir][0]
            yy += DIRS[dir][1]+DIRS_OUT[dir][1]
            dir = (dir + 3) % 4            
        else:
            dir = (dir + 1) % 4
    
    return sides

def fill_perimeter(region, areaFound, sides):
    for x in range(1, len(grid)-1):
        for y in range(1, len(grid[0])-1):
            if regions[x][y] == region:
                perimeter[x][y] = sides
                area[x][y] = areaFound

def flood_fill_outside(x, y, region):
    if outOfBoundsXY(x, y):
        return
    if regions[x][y] == region:
        return
    if grid[x][y] == '#':
        return
    if visitedOutside[x][y]:
        return
    visitedOutside[x][y] = 1

    grid[x][y] = '#'
    
    flood_fill_outside(x-1, y, region)
    flood_fill_outside(x+1, y, region)
    flood_fill_outside(x, y-1, region)
    flood_fill_outside(x, y+1, region)

def flood_fill_inside(x, y, region):
    if outOfBoundsXY(x, y):
        return
    if grid[x][y] == '#':
        return
    if regions[x][y] == region:
        grid[x][y] = '#'
    if visitedInside[x][y]:
        return
    visitedInside[x][y] = 1
    
    flood_fill_inside(x-1, y, region)
    flood_fill_inside(x+1, y, region)
    flood_fill_inside(x, y-1, region)
    flood_fill_inside(x, y+1, region)


AREA_MASK = 1
PERIMETER_IN_MASKS = [2, 4, 8, 16]
PERIMETER_OUT_MASKS = [32, 64, 128, 256]
FLOOD_FILL_MASK = 512
FINAL_PASS_MASK = 1024

DIRS = [
    [-1, 0],
    [0, +1],
    [+1, 0],
    [0, -1]
]

DIRS_OUT = [
    [0, -1],
    [-1, 0],
    [0, +1],
    [+1, 0]
]

f = open('input.txt')

total = 0
grid = [list('.' + line.strip() + '.') for line in f]
grid = [list('.' * len(grid[0]))] + grid + [list('.' * len(grid[0]))]
# print(grid)

visited = [[0 for j in range(len(grid[0]))] for i in range(len(grid))]
perimeter = [[0 for j in range(len(grid[0]))] for i in range(len(grid))]
area = [[0 for j in range(len(grid[0]))] for i in range(len(grid))]
nRegions = 0
regions = [[0 for j in range(len(grid[0]))] for i in range(len(grid))]
for x in range(1, len(grid)-1):
    for y in range(1, len(grid[0])-1):
        if not visited[x][y] & AREA_MASK:
            nRegions += 1
            areaFound = flood_fill_area(x, y, grid[x][y], nRegions)
        if not (visited[x][y] & PERIMETER_OUT_MASKS[1]) and grid[x][y-1] != grid[x][y] and grid[x-1][y] != grid[x][y]:
            sides = calculate_outside_perimeter(x, y, regions[x][y])
            fill_perimeter(nRegions, areaFound, sides)


perimeters = [0 for i in range(nRegions+1)]
areas = [0 for i in range(nRegions+1)]
visitedRegion = [0 for i in range(nRegions+1)]
for region in range(1, nRegions+1):
    print(region)
    for x in range(1, len(grid)-1):
        for y in range(1, len(grid[0])-1):
            if not visitedRegion[region] and regions[x][y] == region:
                visitedRegion[region] = 1
                perimeters[region] = perimeter[x][y]
                areas[region] = area[x][y]
                gridBkp = deepcopy(grid)
                visitedOutside = [[0 for j in range(len(grid[0]))] for i in range(len(grid))]
                flood_fill_outside(0, 0, region)
                visitedInside = [[0 for j in range(len(grid[0]))] for i in range(len(grid))]
                flood_fill_inside(x, y, region)
                sides = 0
                for xx in range(1, len(grid)-1):
                    for yy in range(1, len(grid[0])-1):
                        if grid[xx][yy] != '#':
                            sides += perimeter[xx][yy]
                            visitedInside = [[0 for j in range(len(grid[0]))] for i in range(len(grid))]
                            flood_fill_inside(xx, yy, regions[xx][yy])
                perimeters[region] += sides
                # print(region, grid)
                grid = deepcopy(gridBkp)

# for region in range(1, nRegions+1):
#     for xx in range(1, len(grid)-1):
#         for yy in range(1, len(grid[0])-1):
#             if regions[xx][yy] == region:
#                 print('*', end='')
#             else:
#                 print('.', end='')
#         print()
    # print(region, areas[region], perimeters[region])
    # input()


# print(perimeter)
# print(perimeters)
# print(areas)

total = 0
for i in range(nRegions + 1):
    total += areas[i] * perimeters[i]
print(total)