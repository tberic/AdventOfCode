from aoc import *
from functools import lru_cache
import sys

@lru_cache(maxsize=None)
def walk(y, x, steps):
    global grid, visited

    if grid[y % m][x % n] == '#':
        return 0

    if steps == 0:
        if (y, x) not in visited:
            visited.add( (y, x) )
            return 1
        else:
            return 0

    return walk(y - 1, x, steps-1) + walk(y + 1, x, steps-1) + walk(y, x - 1, steps-1) + walk(y, x + 1, steps-1)


f = open('input.txt', 'r')
grid = [line.strip() for line in f]

startY, startX = 0, 0
for i, line in enumerate(grid):
    if 'S' in line:
        startY = i
        startX = line.index('S')
        break

# print(startY, startX)
m = len(grid)
n = len(grid[0])
visited = set()

sys.setrecursionlimit(100000)
print( walk(startY, startX, 500) )

# for yy in range(m):
#     for xx in range(n):

#         print(yy, xx, end=' ')
        
#         visited = set()
#         Q = [(yy, xx, m)] # 26501365

#         positions = 0
#         while Q:
#             y, x, steps = Q.pop(0)

#             if (y, x, steps) in visited:
#                 continue

#             visited.add( (y, x, steps) )

#             if steps == 0:
#                 positions += 1
#                 continue

#             if grid[(y - 1) % m][x % n] != '#':
#                 Q.append( (y - 1, x, steps-1) )
#             if grid[(y + 1) % m][x % n] != '#':
#                 Q.append( (y + 1, x, steps-1) )        
#             if grid[y % m][(x - 1) % n] != '#':
#                 Q.append( (y, x - 1, steps-1) )
#             if grid[y % m][(x + 1) % n] != '#':
#                 Q.append( (y, x + 1, steps-1) )

#         print(positions)