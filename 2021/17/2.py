import re

def fire(vx, vy):
	global x1, x2, y1, y2
	
	x, y = (0, 0)
	maxHeight = 0
	while x <= x2 and y >= y1:
		
		#print(x, y)
		if y > maxHeight:
			maxHeight = y
		
		if x >= x1 and y <= y2:
			return True, maxHeight
		x += vx
		y += vy
		if vx > 0:
			vx -= 1
		elif vx < 0:
			vx += 1
		vy -= 1
			
	return False, 0
	

f = open('input.txt', 'r')
line = list(f)[0].strip()
m = re.match(r'target area: x\=(\-?\d+)\.\.(\-?\d+), y\=(\-?\d+)\.\.(\-?\d+)', line)
x1 = int(m.group(1))
x2 = int(m.group(2))
y1 = int(m.group(3))
y2 = int(m.group(4))

#(x1, x2) = (20, 30)
#(y1, y2) = (-10, -5)

count = 0
for vx in range(1, x2+1):
	if vx*(vx+1)//2 >= x1:
		for vy in range(y1, 10**3):
			res, h = fire(vx, vy)
			if res:
				count += 1
		
print(count)

f.close()
