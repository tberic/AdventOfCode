import heapq

def outOfBounds(y, x):
    if y < 0 or x < 0:
        return True
    if y >= M or x >= N:
        return True
    return False

def dijkstra(NSTEPS):
    visited = [[0 for j in range(N)] for i in range(M)]
    # BFS
    Q = []
    heapq.heapify(Q)
    heapq.heappush(Q, [0, 0, 0] )
    while Q:
        step, y, x = heapq.heappop(Q)
        # print(step)

        if outOfBounds(y, x):
            continue

        if (y, x) in blocks[:NSTEPS]:
            continue

        if visited[y][x]:
            continue
        visited[y][x] = 1

        if y == M-1 and x == N-1:
            # print(step)
            return True

        Q.append( (step+1, y-1, x) )
        Q.append( (step+1, y+1, x) )
        Q.append( (step+1, y, x-1) )
        Q.append( (step+1, y, x+1) )
    
    return False


f = open('input.txt')

# M = 7
# N = 7
M = 71
N = 71
MAXSTEPS = 1024

# grid = [[0 for j in range(N)] for i in range(M)]
blocks = []
for line in f:
    x, y = list(map(int, line.strip().split(',')))
    blocks.append((y, x))
    # grid[y][x] = 1

stepLeft = MAXSTEPS
stepRight = len(blocks)-1
while stepLeft < stepRight:
    step = (stepLeft + stepRight) // 2
    print(step)
    res = dijkstra(step)
    if not res:
        stepRight = step - 1
    else:
        stepLeft = step + 1

print(stepLeft, stepRight)
print(dijkstra(stepLeft))
print(dijkstra(stepLeft+1))

print(blocks[stepLeft])

# for step in range(MAXSTEPS, len(blocks)+1):
#     print(step, end=' ')
#     if not dijkstra(step):
#         print('Found: ' + str(step))
#         break


# for y in range(M):
#     for x in range(N):
#         print(grid[y][x][1], end='')
#     print()