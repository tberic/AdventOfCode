f = open('input.txt', 'r')

lines = [line.strip() for line in f]
_, initial = lines[0].split(': ')
	
rules = {}
for i in range(2, len(lines)):
	a, b = lines[i].split(' => ')
	rules[a] = b	

f.close()

#print(initial)
#print(initial.count('#'))

s = 0
zero = 0
gen = '..' + initial + '..'
zero += 2
count = 0
for step in range(20):
	#print(step)
	print(gen)
	count += gen.count('#')
	next = list(gen)

	for i in range(2, len(gen)-2):
		#if gen[i-2:i+3] in rules:
		next[i] = rules[ gen[i-2:i+3] ]
		#else:
		#	next[i] = '.'

	gen = '..' + "".join(next) + '..'
	zero += 2

s = 0
for i in range(len(gen)):
	if gen[i] == '#':
		s += i-zero

#print(gen[zero-4:])
print(s)

#print(count)