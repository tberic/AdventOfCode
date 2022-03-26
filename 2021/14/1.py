from collections import Counter

f = open('input.txt', 'r')

lines = [line.strip() for line in f]
template = lines[0]
pairs = {}

for i in range(2, len(lines)):
	pairs[ lines[i].split(' -> ')[0] ] = lines[i].split(' -> ')[1]
    
#print(template)
#print(pairs)

for step in range(10):
	s = ""
	for i in range(len(template)-1):
		pair = template[i]+template[i+1]
		s += template[i] + pairs.get(pair)
	s += template[-1]
	template = s
	#print(template)

c = Counter(template)
a = sorted(c.items(), key=lambda x: x[1])
print(a[-1][1]-a[0][1])


f.close()
