f = open('input.txt', 'r')

x = []
for line in f:
	for num in line.split(','):
		x.append(int(num))

a = min(x)
b = max(x)
m = b*len(x)

for y in range(a, b+1):
	sum = 0
	for i in x:
		sum += abs(i-y)
	if (sum < m):
		m = sum

print(m)

f.close()
