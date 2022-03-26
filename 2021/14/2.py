from collections import Counter, defaultdict
import string

count = defaultdict(list)
visited = defaultdict(list)
for a in string.ascii_uppercase:
	for b in string.ascii_uppercase:
		visited[a+b, 0] = 1
		d = [0 for i in range(26)]
		d[ord(a)-ord('A')] += 1
		d[ord(b)-ord('A')] += 1
		count[a+b, 0] = d
		for s in range(1, 40):
			visited[a+b, s] = 0
			count[a+b, s] = [0 for i in range(26)]				
				
f = open('input.txt', 'r')

lines = [line.strip() for line in f]
template = lines[0]
pairs = {}
for i in range(2, len(lines)):
	pairs[ lines[i].split(' -> ')[0] ] = lines[i].split(' -> ')[1]
    
def polymerize(pair, step):
	global count, visited, pairs
	
	if visited[pair, step]:
		return count[pair, step]

	#print(pair, step, end= ' ')
	#print(count[pair, step])

	visited[pair, step] = 1
	count[pair, step] = [sum(x) for x in zip(polymerize(pair[0]+pairs[pair], step-1), polymerize(pairs[pair]+pair[1], step-1))]
	count[pair, step][ord(pairs[pair])-ord('A')] -= 1

	return count[pair, step]

total = polymerize(template[0]+template[1], 40)
for i in range(1, len(template)-1):
	c = polymerize(template[i]+template[i+1], 40)
	total = [sum(x) for x in zip(total, c)]
	total[ord(template[i])-ord('A')] -= 1

min = max(total)
for x in total:
	if x > 0 and x < min:
		min = x
		
print(max(total)-min)

f.close()
