f = open('input.txt', 'r')

s = 0
for line in f:
    s += int(line)
print(s)

f.close()