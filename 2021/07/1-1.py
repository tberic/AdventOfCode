f = open('input.txt', 'r')

x = []
for line in f:
	for num in line.split(','):
		x.append(int(num))

x.sort()
n = len(x)
y = x[n//2]

sum = 0
for i in x:
        sum += abs(i-y)
print(sum)

f.close()
