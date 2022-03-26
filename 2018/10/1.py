import re

f = open('input.txt', 'r')
p = []
v = []
minx, maxx, miny, maxy = (0, 0, 0, 0)
for line in f:	
	m = re.match(r'position=<(.+), (.+)> velocity=<(.+), (.+)>', line.strip())
	x, y, a, b = list(map(int, m.groups()))
	
	minx = min(minx, x)
	maxx = max(maxx, x)
	miny = min(miny, y)
	maxy = max(maxy, y)
	
	p.append( [x, y] )
	v.append( [a, b] )
f.close()

#print(minx, maxx, miny, maxy)

#the first time before the difference between min and max starts to increase
steps = 0
while steps < 10946:
	steps += 1
	minx, maxx, miny, maxy = (0, 0, 0, 0)
	
	for i in range(len(p)):
		p[i][0] += v[i][0]
		p[i][1] += v[i][1]

		minx = min(minx, p[i][0])
		maxx = max(maxx, p[i][0])
		miny = min(miny, p[i][1])
		maxy = max(maxy, p[i][1])

	#print(minx, maxx, miny, maxy)
#	if maxx-minx < 250 and maxy-miny < 250:
#		print(steps)
#		break

grid = [[ '.' for x in range(minx, maxx+1)] for y in range(miny, maxy+1)]
for x,y in p:
	grid[y][x] = '#'
	
g = open('output.txt', 'w')	
for y in range(miny, maxy+1):
	for x in range(minx, maxx+1):	
		print(grid[y][x], end='', file=g)
	print(file=g)
	
g.close()
