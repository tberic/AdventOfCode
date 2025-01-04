from copy import deepcopy

import sys
sys.setrecursionlimit(1000000)

def outOfBounds(x, y):
    return grid[x][y] == '.'

def flood_fill_area(x, y, crop, id):
    if outOfBounds(x, y):
        return 0
    if grid[x][y] != crop:
        return 0
    if regions[x][y]:
        return 0
    
    regions[x][y] = id
    
    return 1 + flood_fill_area(x-1, y, crop, id) + flood_fill_area(x+1, y, crop, id) \
        + flood_fill_area(x, y-1, crop, id) + flood_fill_area(x, y+1, crop, id)

f = open('input.txt')

total = 0
grid = [list('.' + line.strip() + '.') for line in f]
grid = [list('.' * len(grid[0]))] + grid + [list('.' * len(grid[0]))]

perimeters = [0]
areas = [0]

nRegions = 0
regions = [[0 for j in range(len(grid[0]))] for i in range(len(grid))]
for x in range(1, len(grid)-1):
    for y in range(1, len(grid[0])-1):
        if not regions[x][y]:
            nRegions += 1
            areaFound = flood_fill_area(x, y, grid[x][y], nRegions)
            areas.append(areaFound)
            perimeters.append(0)

print(regions)

for region in range(1, nRegions+1):
    for x in range(1, len(regions)):
        for y in range(1, len(regions[0])):
            count = (regions[x][y] == region) + (regions[x-1][y] == region) +\
                    (regions[x][y-1] == region) + (regions[x-1][y-1] == region)
            if count == 1 or count == 3:
                perimeters[region] += 1
            if count == 2:
                if (regions[x][y] == region and regions[x-1][y-1] == region) or \
                   (regions[x-1][y] == region and regions[x][y-1] == region):
                    perimeters[region] += 2

# for region in range(1, nRegions+1):
#     for xx in range(1, len(grid)-1):
#         for yy in range(1, len(grid[0])-1):
#             if regions[xx][yy] == region:
#                 print('*', end='')
#             else:
#                 print('.', end='')
#         print()
#     print(region, areas[region], perimeters[region])
#     input()

print(areas)
print(perimeters)

total = 0
for i in range(nRegions + 1):
    total += areas[i] * perimeters[i]
print(total)