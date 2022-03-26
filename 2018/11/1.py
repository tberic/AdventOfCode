def powerLevel(x, y, serial):
	return ( ( (x + 10)**2*y + serial*(x + 10) ) % 1000 ) // 100 - 5

serial = 9435
#serial = 18

grid = [[ powerLevel(x, y, serial) for x in range(301) ] for y in range(301) ]

maxLevel = 0
posx, posy = 0, 0
for y in range(1, 301-3):
	for x in range(1, 301-3):
		s = 0
		for j in range(3):
			for i in range(3):
				s += grid[y+j][x+i]
		if s > maxLevel:
			maxLevel = s
			posx = x
			posy = y

print(maxLevel, posx, posy)
