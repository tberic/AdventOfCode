def powerLevel(x, y, serial):
	return ( ( (x + 10)**2*y + serial*(x + 10) ) % 1000 ) // 100 - 5

serial = 9435
#serial = 18

grid = [[ powerLevel(x, y, serial) for x in range(301) ] for y in range(301) ]
levels = [row[:] for row in grid]

maxLevel = 0
posx, posy, maxSize = 0, 0, 0
for size in range(1, 301):
	print(size)
	for y in range(1, 301-size):
		for x in range(1, 301-size):
			s = 0
			for i in range(x, x+size+1):
				s += grid[y][i]
			for i in range(y+1, y+size+1):
				s += grid[i][x]
			levels[y][x] = levels[y+1][x+1] + s
			
			if levels[y][x] > maxLevel:
				maxLevel = levels[y][x]
				posx = x
				posy = y
				maxSize = size

print(maxLevel, posx, posy, maxSize+1)
