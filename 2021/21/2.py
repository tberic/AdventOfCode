hist = { 3: 1, 4: 3, 5: 6, 6: 7, 7: 6, 8: 3, 9: 1 }

def move(n, m=10):
	if n <= m:
		return n
	elif n%m == 0:
		return 10
	else:
		return n%m

def universes1(p1, p2, x, y):
	global hist, player1

	if p1 >= 21:
		return 1
	if p2 >= 21:
		return 0

	if player1[p1][p2][x-1][y-1]:
		return player1[p1][p2][x-1][y-1]
	
	sum = 0
	for i in range(3, 10):
		a = move(x+i)
		if p1 + a >= 21:
			sum += hist[i]
		else:
			for j in range(3, 10):
				b = move(y+j)
				sum += universes1(p1 + a, p2 + b, a, b) * hist[i] * hist[j]
	player1[p1][p2][x-1][y-1] = sum
	return sum

def universes2(p1, p2, x, y):
	global hist, player2

	if p2 >= 21:
		return 1
	if p1 >= 21:
		return 0

	if player2[p1][p2][x-1][y-1]:
		return player2[p1][p2][x-1][y-1]
	
	sum = 0
	for i in range(3, 10):
		a = move(x+i)
		if p1 + a >= 21:
			pass
		else:
			for j in range(3, 10):
				b = move(y+j)
				sum += universes2(p1 + a, p2 + b, a, b) * hist[i] * hist[j]
	player2[p1][p2][x-1][y-1] = sum
	return sum


f = open('input.txt', 'r')
lines = [line.strip() for line in f]
x = int(lines[0][-1:])
y = int(lines[1][-1:])
f.close()

player1 = [ [ [ [0 for i in range(10)] for j in range(10) ] for k in range(21)] for l in range(21)]
player2 = [ [ [ [0 for i in range(10)] for j in range(10) ] for k in range(21)] for l in range(21)]

print(universes1(0, 0, x, y))
print(universes2(0, 0, x, y))
