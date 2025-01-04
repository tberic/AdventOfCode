f = open('input.txt', 'r')
lines = [int(line) for line in f]
f.close()

i = 0
steps =  0
while 0 <= i < len(lines):
    j = i
    offset = lines[i]
    i = i + lines[i]
    if offset >= 3:
        lines[j] -= 1
    else:
        lines[j] += 1
    steps += 1

print(steps)