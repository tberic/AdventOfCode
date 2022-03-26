f = open('input.txt', 'r')
lines = [line.strip() for line in f]
n = len(lines)
f.close()

neighbors = {}

for line in lines:
    left, right = line.split(' <-> ')
    a = int(left)
    neighbors[int(left)] = [int(x) for x in right.split(', ')]

visited = set()
S = [0]
while S:
    x = S.pop()
    if x in visited:
        continue

    visited.add(x)

    for y in neighbors[x]:
        S.append(y)

print(len(visited))