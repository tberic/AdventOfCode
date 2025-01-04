import re

N = 1000
grid = [[0 for j in range(N+1)] for i in range(N+1)]

f = open('input.txt', 'r')

for line in f:
    m = re.match(r'#(\d+) @ (\d+),(\d+): (\d+)x(\d+)', line.strip())
    id, x, y, a, b = list(map(int, m.groups()))
    #print(id, x, y, a, b)
    for i in range(x, x+a):
        for j in range(y, y+b):
            grid[i][j] += 1

f.close()

count = 0
for i in range(N+1):
    for j in range(N+1):
        if grid[i][j] > 1:
            count += 1

print(count)