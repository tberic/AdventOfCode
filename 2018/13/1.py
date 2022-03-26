def cartGrid(x, y):
	global cart
	for i in range(len(cart)):
		if cart[i][0] == x and cart[i][1] == y:
			return cart[i][2]
	return False

def printGrid():
	global grid
	for i in range(len(grid)):
		for j in range(len(grid[i])):
			if cartGrid(i, j):
				print(cartGrid(i, j), end='')
			else:
				print(grid[i][j], end='')
		print()
	print()


dir = { 'v': (+1, 0), '^': (-1, 0), '<': (0, -1), '>': (0, +1) }
dirs = "<^>v"

f = open('input.txt', 'r')
grid = [list(line[:-1]) for line in f]
f.close()

cart = []
for i in range(len(grid)):
	for j in range(len(grid[i])):
		if grid[i][j] in ['v', '^', '<', '>']:
			cart.append([ i, j, grid[i][j], 0 ])
			if grid[i][j] in ['v', '^']:
				grid[i][j] = '|'
			else:
				grid[i][j] = '-'

while True:
	# move the carts
	for i in range(len(cart)):
		cart[i][0] += dir[cart[i][2]][0]
		cart[i][1] += dir[cart[i][2]][1]

	# change directions if needed
	for i in range(len(cart)):
		if cart[i][2] == '^' and grid[ cart[i][0] ][ cart[i][1] ] == '/':
			cart[i][2] = '>'
		elif cart[i][2] == '^' and grid[ cart[i][0] ][ cart[i][1] ] == '\\':
			cart[i][2] = '<'
		elif cart[i][2] == 'v' and grid[ cart[i][0] ][ cart[i][1] ] == '\\':			
			cart[i][2] = '>'
		elif cart[i][2] == 'v' and grid[ cart[i][0] ][ cart[i][1] ] == '/':
			cart[i][2] = '<'
		elif cart[i][2] == '<' and grid[ cart[i][0] ][ cart[i][1] ] == '/':
			cart[i][2] = 'v'
		elif cart[i][2] == '<' and grid[ cart[i][0] ][ cart[i][1] ] == '\\':
			cart[i][2] = '^'
		elif cart[i][2] == '>' and grid[ cart[i][0] ][ cart[i][1] ] == '\\':
			cart[i][2] = 'v'
		elif cart[i][2] == '>' and grid[ cart[i][0] ][ cart[i][1] ] == '/':
			cart[i][2] = '^'
		elif grid[ cart[i][0] ][ cart[i][1] ] == '+':
			cart[i][2] = dirs[ (dirs.find(cart[i][2])+3+cart[i][3]) % 4 ]
			cart[i][3] = (cart[i][3]+1)%3

	# check for collisions
	done = False
	for i in range(len(cart)):
		if done:
			break
		for j in range(len(cart)):
			if i != j and cart[i][0] == cart[j][0] and cart[i][1] == cart[j][1]:
				print(f'{cart[i][1]},{cart[i][0]}')
				done = True
				break
	if done:
		break