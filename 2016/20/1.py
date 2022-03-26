f = open('input.txt', 'r')
a = [ list(map(int, line.strip().split('-'))) for line in f ]
f.close()

a.sort()

b = []
i = 0
while i < len(a):
    j = i+1
    x = a[i][0]
    y = a[i][1]
    while j < len(a) and a[j][0] <= y+1:
        y = max(a[j][1], y)
        j += 1
    b.append([x, y])
    i = j

print(len(b))

g = open('input-reduced.txt', 'w')
for x in b:
    print(f'{x[0]}-{x[1]}', file=g)
g.close()