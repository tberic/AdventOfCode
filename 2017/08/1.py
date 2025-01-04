f = open('input.txt', 'r')
lines = [line.strip() for line in f]
f.close()

reg = {}

maxEver = 0
for line in lines:
    a, instr, n, _, b, op, y = line.split()
    n = int(n)
    y = int(y)

    if a not in reg:
        reg[a] = 0
    if b not in reg:
        reg[b] = 0

    x = reg[b]
    if eval(str(x) + op + str(y)):
        if instr == "inc":
            reg[a] += n
            if reg[a] > maxEver:
                maxEver = reg[a]
        elif instr == "dec":
            reg[a] -= n

print(max(reg.values()))
print(maxEver)