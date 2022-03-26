def move(n, m=10):
	if n <= m:
		return n
	elif n%m == 0:
		return 10
	else:
		return n%m
	

f = open('input.txt', 'r')
lines = [line.strip() for line in f]
x = int(lines[0][-1:])
y = int(lines[1][-1:])
f.close()

die = 0
player1 = 0
player2 = 0
nRolls = 0
i = 0
while player1 < 1000 and player2 < 1000:
	i += 1
	a = 0
	for _ in range(3):
		die = move(die+1, 100)
		a += die
	x = move(x+a)
	player1 += x
	nRolls += 3
	
	if player1 >= 1000:
		break
	
	b = 0	
	for _ in range(3):
		die = move(die+1, 100)
		b += die
	nRolls += 3
	y = move(y+b)
	player2 += y
	
	print(str(i)+': '+str(player1)+' '+str(player2))
	
print(x, y)
	
if player1 >= 1000:
	print(player2*nRolls)
else:
	print(player1*nRolls)
