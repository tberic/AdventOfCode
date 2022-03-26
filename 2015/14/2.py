import re

name = {}
speed = [0 for i in range(9)]
time = [0 for i in range(9)]
rest = [0 for i in range(9)]

f = open('input.txt', 'r')
n = 0
for line in f:
    m = re.search(r'(.*) can fly (\d+) km/s for (\d+) seconds, but then must rest for (\d+) seconds\.', line)
    a, v, t, r = m.groups()
    if a not in name:
        name[a] = n
        n += 1
    speed[name[a]] = int(v)
    time[name[a]] = int(t)
    rest[name[a]] = int(r)
f.close()

T = 2503
dist = [0 for i in range(n)]
points = [0 for i in range(9)]
for t in range(T):
    for i in range(n):
        if t%(time[i]+rest[i]) < time[i]:
            dist[i] += speed[i]

    m = max(dist)
    for i in range(n):
        if dist[i] == m:
            points[i] += 1
    print(dist)
    print(points)

points.sort()
print(points[-1])