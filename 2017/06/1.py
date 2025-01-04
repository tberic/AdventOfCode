def convert():
    global reg, N
    s = 0
    for k in range(len(reg)):
        s = s*N + reg[k]
    return s

f = open('input.txt', 'r')
reg = list(map(int, f.readline().strip().split()))
f.close()

N = sum(reg) + 1

seen = {}

steps = 0
while True:
    x = convert()
    if x in seen:
        break
    seen[x] = steps
    
    m = max(reg)
    i = reg.index(m)

    reg[i] = 0
    a = m // len(reg)
    b = m % len(reg)
    if a > 0:
        for k in range(len(reg)):
            reg[k] += a

    k = (i+1) % len(reg)
    while b > 0:
        reg[k] += 1
        k = (k+1) % len(reg)
        b -= 1

    steps += 1

print(steps)
print(steps - seen[x])