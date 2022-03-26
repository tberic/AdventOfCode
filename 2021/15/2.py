from queue import PriorityQueue

def modify(x):
    if x <= 9:
        return x
    else:
        return x%9

f = open('input_large.txt', 'r')

grid = []
for line in f:
    a = [int(x) for x in line.strip()]
    grid.append(a)
n = len(grid)

inf = 10**10
risk = [[inf for i in range(n)] for j in range(n)]
risk[0][0] = 0
visited = [[0 for i in range(n)] for j in range(n)]

pq = PriorityQueue()
pq.put((0, 0, 0))

while not pq.empty():
	(dist, x, y) = pq.get()
	visited[x][y] = 1

	if (x > 0 and not visited[x-1][y]):
		d = risk[x][y] + grid[x-1][y]
		if d < risk[x-1][y]:
			risk[x-1][y] = d
			pq.put( (d, x-1, y) )
	if (x < n-1 and not visited[x+1][y]):
		d = risk[x][y] + grid[x+1][y]
		if d < risk[x+1][y]:
			risk[x+1][y] = d
			pq.put( (d, x+1, y) )
	if (y > 0 and not visited[x][y-1]):
		d = risk[x][y] + grid[x][y-1]
		if d < risk[x][y-1]:
			risk[x][y-1] = d
			pq.put( (d, x, y-1) )
	if (y < n-1 and not visited[x][y+1]):
		d = risk[x][y] + grid[x][y+1]
		if d < risk[x][y+1]:
			risk[x][y+1] = d
			pq.put( (d, x, y+1) )

print(risk[n-1][n-1])

#for i in range(n):
#    for j in range(n):
#        print(risk[i][j], end=' ')
#    print()

f.close()
