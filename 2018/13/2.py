def checkCollision(i):
	global cart, nAlive
	# check for collisions
	j = 0
	while j < len(cart):
		if i != j and cart[j][4] and cart[i][0] == cart[j][0] and cart[i][1] == cart[j][1]:
			cart[j][4] = 0
			cart[i][4] = 0
			nAlive -= 2
			return
		j += 1


dir = { 'v': (+1, 0), '^': (-1, 0), '<': (0, -1), '>': (0, +1) }
dirs = "<^>v"

f = open('input.txt', 'r')
grid = [list(line[:-1]) for line in f]
f.close()

cart = []
for i in range(len(grid)):
	for j in range(len(grid[i])):
		if grid[i][j] in ['v', '^', '<', '>']:
			cart.append([ i, j, grid[i][j], 0, 1 ])
			if grid[i][j] in ['v', '^']:
				grid[i][j] = '|'
			else:
				grid[i][j] = '-'

nAlive = len(cart)

#sorted(cart, key=lambda x: (x[1], x[0]))
#print(cart)

while nAlive > 1:
	# move the carts

	cart = sorted(cart, key=lambda x: (x[1], x[0]))

	i = 0
	while i < len(cart):
		if cart[i][4]:
			cart[i][0] += dir[cart[i][2]][0]
			cart[i][1] += dir[cart[i][2]][1]
			r = checkCollision(i)
		i += 1

	# change directions if needed
	for i in range(len(cart)):
		if cart[i][4]:
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

print(cart)