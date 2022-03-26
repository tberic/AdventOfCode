f = open('input.txt', 'r')

lines = [line.strip() for line in f]
_, initial = lines[0].split(': ')
	
rules = {}
for i in range(2, len(lines)):
	a, b = lines[i].split(' => ')
	rules[a] = b	

f.close()

s = 0
zero = 0
gen = '....' + initial + '....'
zero += 4
count = 0
for step in range(300):
	#print(step, zero, end = ' ')
	#print(gen)
	count += gen.count('#')
	next = list(gen)

	for i in range(2, len(gen)-2):
		if gen[i-2:i+3] in rules:
			next[i] = rules[ gen[i-2:i+3] ]
		else:
			next[i] = '.'

	# remove all the dots from the beginning and the end (keep track of the zero position) and later add two dots on each end
	i = 0
	if next[i] == '.':
		while i < len(next) and next[i] == '.':
			i += 1
		zero -= i
	j = len(next)
	if next[j-1] == '.':
		while j >= 0 and next[j-1] == '.':
			j -= 1
	next = next[i:j]

	gen = '....' + "".join(next) + '....'
	zero += 4

print(gen)
print(zero, len(gen))
print(gen.count('#'))
zero -= 50*10**9 - 300
s = 0
for i in range(len(gen)):
	if gen[i] == '#':
		s += i-zero
print(s)