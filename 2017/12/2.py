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

components = 0
while True:
    done = 1
    for x in range(n):
        if x not in visited:
            S = [x]
            done = 0
            break
    if done:
        break

    components += 1

    while S:
        x = S.pop()
        if x in visited:
            continue

        visited.add(x)

        for y in neighbors[x]:
            S.append(y)

print(components)