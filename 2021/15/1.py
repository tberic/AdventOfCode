def find_min(l):
    global risk, inf

    min = inf+1
    el = (0, 0)
    for x in l:
        if risk[x[0]][x[1]] < min:
            min = risk[x[0]][x[1]]
            el = x
    return el

f = open('input.txt', 'r')

grid = []
for line in f:
    a = [int(x) for x in line.strip()]
    grid.append(a)

n = len(grid)
inf = 10**10
risk = [[inf for i in range(n)] for j in range(n)]
risk[0][0] = 0

Q = set()
Q.add((0, 0))

for x in range(n):
    for y in range(n):
        if x != 0 or y != 0:
            risk[x][y] = inf
            Q.add((x, y))

while Q:
    u = find_min(Q)
    x,y = u
    Q.remove(u)
    
    if (x > 0 and (x-1,y) in Q):
        d = risk[x][y] + grid[x-1][y]
        if d < risk[x-1][y]:
            risk[x-1][y] = d
    if (x < n-1 and (x+1,y) in Q):
        d = risk[x][y] + grid[x+1][y]
        if d < risk[x+1][y]:
            risk[x+1][y] = d
    if (y > 0 and (x,y-1) in Q):
        d = risk[x][y] + grid[x][y-1]
        if d < risk[x][y-1]:
            risk[x][y-1] = d
    if (y < n-1 and (x,y+1) in Q):
        d = risk[x][y] + grid[x][y+1]
        if d < risk[x][y+1]:
            risk[x][y+1] = d

print(risk[n-1][n-1])

#for i in range(n):
#    for j in range(n):
#        print(risk[i][j], end=' ')
#    print()

f.close()