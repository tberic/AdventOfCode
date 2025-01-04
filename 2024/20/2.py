import heapq
from collections import defaultdict

DIRS = [
    [-1, 0],
    [+1, 0],
    [0, -1],
    [0, +1]
]

def BFS(y1, x1, dist_arr):
    dist_arr[y1][x1] = 0

    Q = []
    Q.append([y1, x1])
    while Q:
        y, x = Q.pop(0)

        if grid[y][x] == '#':
            continue
        
        for dir in DIRS:
            if dist_arr[y + dir[0]][x + dir[1]] > dist_arr[y][x] + 1 and grid[y + dir[0]][x + dir[1]] != '#':
                Q.append([y + dir[0], x + dir[1]])
                dist_arr[y + dir[0]][x + dir[1]] = dist_arr[y][x] + 1
    
    return -1


f = open('input.txt')

grid = [list(line.strip()) for line in f]
M = len(grid)
N = len(grid[0])
for y in range(M):
    for x in range(N):
        if grid[y][x] == 'S':
            startY, startX = y, x
        elif grid[y][x] == 'E':
            endY, endX = y, x

dist_to_start = [[10 ** 10 for j in range(N)] for i in range(M)]
dist_to_end = [[10 ** 10 for j in range(N)] for i in range(M)]

BFS(startY, startX, dist_to_start)
BFS(endY, endX, dist_to_end)
noCheats = dist_to_start[endY][endX]
# print(dist_from_start[endY][endX])

total = 0
for y1 in range(1, M-1):
    for x1 in range(1, N-1):
        for y2 in range(1, M-1):
            for x2 in range(1, N-1):
                if abs(y1 - y2) + abs(x1 - x2) <= 20:
                    # print(y1, x1, y2, x2)
                    # cheat from (y1, x1) to (y2, x2)
                    t1 = dist_to_start[y1][x1]
                    t2 = abs(y1 - y2) + abs(x1 - x2)
                    t3 = dist_to_end[y2][x2]
        
                    if noCheats - (t1+t2+t3) >= 100:
                        total += 1

print(total)