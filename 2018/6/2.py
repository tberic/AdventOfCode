def dist(T1, T2):
    return abs(T1[0]-T2[0]) + abs(T1[1]-T2[1])

f = open('input.txt', 'r')

points = []

minx, miny = (1000, 1000)
maxx, maxy = (0, 0)
for line in f:
    x, y = list(map(int, line.split(',')))
    points.append([x, y])
    minx = min(minx, x)
    maxx = max(maxx, x)
    miny = min(miny, y)
    maxy = max(maxy, y)
f.close()

print(minx, miny, maxx, maxy)
N = 10000

#grid = [[0 for j in range(N+1)] for i in range(N+1)]

count = 0
for x in range(minx-N, maxx+1+N):
    for y in range(miny-N, maxy+1+N):
        s = 0
        for k in range(len(points)):
            s += dist([x, y], points[k])
            if s >= N:
                break
        if s < N:
            count += 1
print(count)

#         closest = -1
#         d = 10**10
#         tie = 0
#         for k in range(len(points)):
#             if dist([x, y], points[k]) < d:
#                 tie = 0
#                 d = dist([x, y], points[k])
#                 closest = k
#             elif dist([x, y], points[k]) == d:
#                 tie = 1
#         if not tie and not onHull[closest]:
#             grid[x][y] = closest+1
