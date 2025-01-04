f = open('input.txt', 'r')

x = []
for line in f:
	for num in line.split(','):
		x.append(int(num))

a = min(x)
b = max(x)
m = b*(b+1)/2*len(x)

for y in range(a, b+1):
	sum = 0
	for i in x:
		sum += abs(i-y)*(abs(i-y)+1)/2
	if (sum < m):
		m = sum

print(m)

f.close()
