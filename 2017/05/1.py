f = open('input.txt', 'r')
lines = [int(line) for line in f]
f.close()

i = 0
steps =  0
while i < len(lines):
    t = i
    i = i + lines[i]
    lines[t] += 1
    steps += 1

print(steps)