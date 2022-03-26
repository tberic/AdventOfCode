f = open('input.txt', 'r')
ran = { int(line.split(': ')[0]): int(line.split(': ')[1]) for line in f }
n = max(ran.keys())
layer = [0 for i in range(n+1)]
dir = [1 if i in ran else 0 for i in range(n+1) ]
f.close()

s = 0
for i in range(n+1):
    if i in ran and layer[i] == 0:
        s += i*ran[i]
    for j in range(n+1):
        if j in ran:
            layer[j] += dir[j]
            if layer[j] >= ran[j]-1:
                dir[j] = -dir[j]
            elif layer[j] <= 0:
                dir[j] = -dir[j]

print(s)