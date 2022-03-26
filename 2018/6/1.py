def dist(T1, T2):
    return abs(T1[0]-T2[0]) + abs(T1[1]-T2[1])

f = open('input-labeled.txt', 'r')

points = []
onHull = []

minx, miny = (1000, 1000)
maxx, maxy = (0, 0)
for line in f:
    x, y, label = list(map(int, line.split(',')))
    points.append([x, y])
    onHull.append(label)
    minx = min(minx, x)
    maxx = max(maxx, x)
    miny = min(miny, y)
    maxy = max(maxy, y)
f.close()

print(minx, miny, maxx, maxy)
N = max(maxx, maxy)
grid = [[0 for j in range(N+1)] for i in range(N+1)]

for x in range(minx, maxx+1):
    for y in range(miny, maxy+1):
        closest = -1
        d = 10**10
        tie = 0
        for k in range(len(points)):
            if dist([x, y], points[k]) < d:
                tie = 0
                d = dist([x, y], points[k])
                closest = k
            elif dist([x, y], points[k]) == d:
                tie = 1
        if not tie and not onHull[closest]:
            grid[x][y] = closest+1

maxSize = 0
for k in range(len(points)):
    if not onHull[k]:
        s = 0
        for x in range(minx, maxx+1):
            for y in range(miny, maxy+1):
                if grid[x][y] == k+1:
                    s += 1
        if s > maxSize:
            maxSize = s

print(maxSize)