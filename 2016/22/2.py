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

g = open('map.txt', 'w')
for x in range(30):
    for y in range(35):
        c = '/'
        if x > 0 and grid[x-1][y][1] >= grid[x][y][0]:
            c = '^'
        if x < 29 and grid[x+1][y][1] >= grid[x][y][0]:
            c = 'v'
        if y > 0 and grid[x][y-1][1] >= grid[x][y][0]:
            c = '<'
        if y < 34 and grid[x][y+1][1] >= grid[x][y][0]:
            c = '>'
        if grid[x][y][0] == 0:
            c = 'x'

        print(f'{grid[x][y][0]}{c}{grid[x][y][0]+grid[x][y][1]}'.ljust(6), end=' ', file=g)
    print(file=g)
g.close()