f = open('input.txt', 'r')
lines = f.readlines()

grid = [[0 for i in range(1311)] for j in range(1311)]

m = 0
n = 0
for i in range(len(lines)):
    if lines[i].strip() == "":
        k = i+1
        break
    x, y = list(map(int, lines[i].strip().split(',')))
    if x+1 > m:
        m = x+1
    if y+1 > n:
        n = y+1
    grid[x][y] = 1

print(m, n) #m = 1311, n = 893

s, t = lines[k].strip().split('=')
t = int(t)
dir = s[-1]

if dir == 'x':
    m //= 2
    for i in range(m):
        for j in range(n):
            grid[i][j] |= grid[t+m-i][j]
if dir == 'y':
    n //= 2
    for i in range(m):
        for j in range(n):
            grid[i][j] |= grid[i][t+n-j]

sum = 0
for i in range(m):
    for j in range(n):
        sum += grid[i][j]

print(sum)

f.close()
