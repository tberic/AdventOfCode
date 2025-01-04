def outOfBounds(y, x):
    if y < 0 or x < 0:
        return True
    if y >= M or x >= N:
        return True
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

visited = [[0 for j in range(N)] for i in range(M)]

# BFS
Q = [(0, 0, 0)]
while Q:
    step, y, x = Q.pop(0)
    # print(step)

    if outOfBounds(y, x):
        continue

    if (y, x) in blocks[:MAXSTEPS]:
        continue

    if visited[y][x]:
        continue
    visited[y][x] = 1

    if y == M-1 and x == N-1:
        print(step)
        break

    Q.append( (step+1, y-1, x) )
    Q.append( (step+1, y+1, x) )
    Q.append( (step+1, y, x-1) )
    Q.append( (step+1, y, x+1) )


# for y in range(M):
#     for x in range(N):
#         print(grid[y][x][1], end='')
#     print()