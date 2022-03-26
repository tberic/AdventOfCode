import re

f = open('input.txt', 'r')
lines = [line.strip() for line in f]
f.close()

grid = [[(0, 0) for j in range(35)] for i in range(30)]

for s in lines[2:]:
    words = s.split()
    m = re.search(r'x(\d+)\-y(\d+)', words[0])
    x, y = list(map(int, m.groups()))
    used = int(words[2][:-1])
    avail = int(words[3][:-1])
    grid[x][y] = (used, avail)

count = 0
for x in range(30):
    for y in range(35):
        for i in range(30):
            for j in range(35):
                if x != i or y != j:
                    if grid[x][y][0] != 0 and grid[x][y][0] <= grid[i][j][1]:
                        count += 1
print(count)