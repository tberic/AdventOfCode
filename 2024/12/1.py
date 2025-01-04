def outOfBounds(x, y):
    if x < 0 or y < 0:
        return True
    if x >= len(grid):
        return True
    if y >= len(grid[0]):
        return True
    return False

def flood_fill_area(x, y, crop):
    if outOfBounds(x, y):
        return 0
    if grid[x][y] != crop:
        return 0
    if visited[x][y] & AREA_MASK:
        return 0
    
    visited[x][y] |= AREA_MASK
    
    return 1 + flood_fill_area(x-1, y, crop) + flood_fill_area(x+1, y, crop) \
        + flood_fill_area(x, y-1, crop) + flood_fill_area(x, y+1, crop)

def flood_fill_perimeter(x, y, crop):
    if outOfBounds(x, y):
        return 0
    if grid[x][y] != crop:
        return 0
    if visited[x][y] & PERIMETER_MASK:
        return 0
    
    visited[x][y] |= PERIMETER_MASK
    
    count = 0
    for dir in DIRS:
        xx = x+dir[0]
        yy = y+dir[1]
        if outOfBounds(xx, yy) or (not outOfBounds(xx, yy) and grid[xx][yy] != crop):
            count += 1
    
    return count + flood_fill_perimeter(x-1, y, crop) + flood_fill_perimeter(x+1, y, crop) \
        + flood_fill_perimeter(x, y-1, crop) + flood_fill_perimeter(x, y+1, crop)

AREA_MASK = 1
PERIMETER_MASK = 2

DIRS = [
    [-1, 0],
    [+1, 0],
    [0, -1],
    [0, +1]
]

f = open('input.txt')

total = 0
grid = [line.strip() for line in f]
visited = [[0 for j in range(len(grid[0]))] for i in range(len(grid))]
for x in range(len(grid)):
    for y in range(len(grid[0])):
        if not visited[x][y]:
            area = flood_fill_area(x, y, grid[x][y])
            perimeter = flood_fill_perimeter(x, y, grid[x][y])
            # print(area, perimeter)
            total += area * perimeter

print(total)