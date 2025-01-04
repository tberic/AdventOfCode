import heapq

NO_CHEAT = 0
CHEAT = 1

def outOfBounds(y, x):
    if y < 0 or x < 0:
        return True
    if y >= M or x >= N:
        return True
    return False

def dijkstra(y, x):
    visited = [[0 for j in range(N)] for i in range(M)]

    Q = []
    heapq.heapify(Q)
    heapq.heappush(Q, [0, y, x, NO_CHEAT, 20] )
    while Q:
        step, y, x, cheat_used, cheat_duration = heapq.heappop(Q)

        if outOfBounds(y, x):
            continue

        if grid[y][x] == '#' and not cheat_used or (cheat_used and cheat_duration == 0):
            continue
        
        if visited[y][x]:
            continue
        visited[y][x] = 1

        if y == endY and x == endX:
            return step

        if not cheat_used:
            Q.append( (step+1, y-1, x, NO_CHEAT, 20) )
            Q.append( (step+1, y+1, x, NO_CHEAT, 20) )
            Q.append( (step+1, y, x-1, NO_CHEAT, 20) )
            Q.append( (step+1, y, x+1, NO_CHEAT, 20) )
            Q.append( (step, y, x+1, CHEAT, 20) )

        if cheat_used:
            if cheat_duration > 0:
                Q.append( (step+1, y-1, x, CHEAT, cheat_duration - 1) )
                Q.append( (step+1, y+1, x, CHEAT, cheat_duration - 1) )
                Q.append( (step+1, y, x-1, CHEAT, cheat_duration - 1) )
                Q.append( (step+1, y, x+1, CHEAT, cheat_duration - 1) )
            else:
                Q.append( (step+1, y-1, x, CHEAT, 0) )
                Q.append( (step+1, y+1, x, CHEAT, 0) )
                Q.append( (step+1, y, x-1, CHEAT, 0) )
                Q.append( (step+1, y, x+1, CHEAT, 0) )

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

noCheats = dijkstra(startY, startX)
print(noCheats)

total = 0
for y in range(1, M-1):
    for x in range(1, N-1):
        if grid[y][x] == '#':
            grid[y][x] = '.'
            cheat = dijkstra(startY, startX)
            if noCheats - cheat >= 100:
                total += 1
            grid[y][x] = '#'

print(total)