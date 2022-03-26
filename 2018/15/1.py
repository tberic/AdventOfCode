attackStrength = {'G': 3, 'E': 3}

def printGrid():
	global grid, unit, g
	grid2 = [row[:] for row in grid]
	for i in range(len(unit)):
		if unit[i][4]:
			grid2[unit[i][0]][unit[i][1]] = unit[i][3]
	for i in range(len(grid2)):
		print("".join(grid2[i]), file=g)
	print(file=g)


def enemyNear(x, y, c):
	global grid
	return grid[x-1][y] == c or grid[x+1][y] == c or grid[x][y-1] == c or grid[x][y+1] == c


def findUnit(x, y):
	global grid, unit
	for i in range(len(unit)):
		if unit[i][4] and unit[i][0] == x and unit[i][1] == y:
			return i
	return False


def chooseEnemy(i):
	global unit, grid
	enemies = []
	if grid[ unit[i][0]-1 ][ unit[i][1] ] == other[ unit[i][3] ]:
		enemies.append( findUnit(unit[i][0]-1, unit[i][1]) )
	if grid[ unit[i][0] ][ unit[i][1]-1 ] == other[ unit[i][3] ]:
		enemies.append( findUnit(unit[i][0], unit[i][1]-1) )
	if grid[ unit[i][0] ][ unit[i][1]+1 ] == other[ unit[i][3] ]:
		enemies.append( findUnit(unit[i][0], unit[i][1]+1) )
	if grid[ unit[i][0]+1 ][ unit[i][1] ] == other[ unit[i][3] ]:
		enemies.append( findUnit(unit[i][0]+1, unit[i][1]) )
	minHP = 201
	unitID = -1
	for i in enemies:
		if unit[i][2] < minHP:
			minHP = unit[i][2]
			unitID = i
	return unitID


def findClosestEnemy(i):
	global grid
	x = unit[i][0]
	y = unit[i][1]
	
	Q = []
	Q.append( (0, x, y, "") )
	
	dist = [[10**10 for j in range(len(grid[0]))] for i in range(len(grid))]
	dist[x][y] = 0
	
	while Q:
		d, x, y, path = Q.pop(0)
		
		if enemyNear(x, y, other[unit[i][3]]):
			return path[0]
		
		if grid[x-1][y] == '.' and d + 1 < dist[x-1][y]:
			dist[x-1][y] = d + 1
			Q.append((d+1, x-1, y, path+'U'))
		if grid[x][y-1] == '.' and d + 1 < dist[x][y-1]:
			dist[x][y-1] = d + 1
			Q.append((d+1, x, y-1, path+'L'))
		if grid[x][y+1] == '.' and d + 1 < dist[x][y+1]:
			dist[x][y+1] = d + 1
			Q.append((d+1, x, y+1, path+'R'))
		if grid[x+1][y] == '.' and d + 1 < dist[x+1][y]:
			dist[x+1][y] = d + 1
			Q.append((d+1, x+1, y, path+'D'))
	
	return False


def unitsLeft(i):
    global unit
    for j in range(i+1, len(unit)):
        if unit[j][4]:
            return True
    return False


other = {'G': 'E', 'E': 'G' }

g = open('output.txt', 'w')
f = open('input.txt', 'r')
grid = [list(line.strip()) for line in f]
f.close()

# search for goblins and elfs and make a note of their positions
unit = []
nUnits = {'G': 0, 'E': 0}
for i in range(len(grid)):
	for j in range(len(grid[i])):
		if grid[i][j] in ['G', 'E']:
			unit.append([ i, j, 200, grid[i][j], True ]) # x y hp type alive
			nUnits[ grid[i][j] ] += 1

printGrid()

turn = 0
while nUnits['G'] and nUnits['E']:
    turn += 1
    unit = sorted(unit)

    for i in range(len(unit)):
        if unit[i][4]:
            x, y, hp, t, alive = unit[i]
            if not enemyNear(x, y, other[t] ): # move
                # find the closest enemy using Dijsktra's algorithm
                move = findClosestEnemy(i)
                if move:					
                    if move == 'U':
                        grid[x][y] = '.'
                        grid[x-1][y] = t
                        unit[i][0] -= 1
                    elif move == 'L':
                        grid[x][y] = '.'
                        grid[x][y-1] = t
                        unit[i][1] -= 1
                    elif move == 'R':
                        grid[x][y] = '.'
                        grid[x][y+1] = t
                        unit[i][1] += 1
                    elif move == 'D':
                        grid[x][y] = '.'
                        grid[x+1][y] = t
                        unit[i][0] += 1
                    x, y = unit[i][0:2]
                else: # this unit can't reach enemy units
                    pass
            if enemyNear( x, y, other[t] ): # attack
                j = chooseEnemy(i)
                unit[j][2] -= attackStrength[t]
                if unit[j][2] <= 0: # if HP<=0, unit dies
                    nUnits[ other[t] ] -= 1
                    grid[unit[j][0]][unit[j][1]] = '.'
                    unit[j][4] = False
                    if nUnits[ other[t] ] == 0:
                        if unitsLeft(i):
                            turn -= 1
                        break
        
    printGrid()	


print(turn)
print(unit)

s = 0
for x, y, hp, t, alive in unit:
	if alive:
		s += hp
print(turn*s)

g.close()