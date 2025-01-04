import sys

UP = (-1, 0)
DOWN = (+1, 0)
LEFT = (0, -1)
RIGHT = (0, +1)

def hash(dir):
    if dir == UP:
        return 1
    if dir == DOWN:
        return 2
    if dir == LEFT:
        return 4
    if dir == RIGHT:
        return 8
    return 0

def follow(y, x, dir):
    if y < 0 or y >= len(grid):
        return
    if x < 0 or x >= len(grid[0]):
        return
    if visited[y][x] & hash(dir):
        return
    
    visited[y][x] |= hash(dir)

    if grid[y][x] == '.':
        follow(y + dir[0], x + dir[1], dir)
    elif grid[y][x] == '/':
        if dir == UP:
            follow(y, x + 1, RIGHT)
        elif dir == DOWN:
            follow(y, x - 1, LEFT)
        elif dir == RIGHT:
            follow(y - 1, x, UP)
        elif dir == LEFT:
            follow(y + 1, x, DOWN)
    elif grid[y][x] == '\\':
        if dir == UP:
            follow(y, x - 1, LEFT)
        elif dir == DOWN:
            follow(y, x + 1, RIGHT)
        elif dir == RIGHT:
            follow(y + 1, x, DOWN)
        elif dir == LEFT:
            follow(y - 1, x, UP)
    elif grid[y][x] == '-':
        if dir == LEFT or dir == RIGHT:
            follow(y + dir[0], x + dir[1], dir)
        else:
            follow(y, x - 1, LEFT)
            follow(y, x + 1, RIGHT)
    elif grid[y][x] == '|':
        if dir == UP or dir == DOWN:
            follow(y + dir[0], x + dir[1], dir)
        else:
            follow(y - 1, x, UP)
            follow(y + 1, x, DOWN)
    

f = open('input.txt', 'r')

grid = [line.strip() for line in f]
visited = [[0 for j in range(len(grid[0]))] for i in range(len(grid))]

sys.setrecursionlimit(100000)

follow(0, 0, RIGHT)

energized = 0
for y in range(len(grid)):
    for x in range(len(grid[0])):
        if visited[y][x]:
            energized += 1
print(energized)

# for y in range(len(visited)):
#     for x in range(len(visited[0])):
#         print(visited[y][x], end=' ')
#     print()
