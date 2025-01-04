import re
import itertools

f = open('input.txt', 'r')

N = 8
dist = [[0 for i in range(N)] for j in range(N)]

city = {}

n = 0
for line in f:
    m = re.search(r'(.*) to (.*) = (\d+)', line.strip())
    a, b, d = m.groups()
    if a not in city:
        city[a] = n
        n += 1
    if b not in city:
        city[b] = n
        n += 1
    dist[city[a]][city[b]] = int(d)
    dist[city[b]][city[a]] = int(d)

f.close()

minDist = 10**10
maxDist = 0
for p in itertools.permutations(range(n)):
    d = 0
    for i in range(len(p)-1):
        d += dist[p[i]][p[i+1]]
    if d < minDist:
        minDist = d
    if d > maxDist:
        maxDist = d

print(minDist, maxDist)