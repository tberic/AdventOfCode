f = open('input.txt', 'r')
line = f.readline().strip()
f.close()

s = 0
for i in range(len(line)-1):
    if line[i] == line[i+1]:
        s += int(line[i])

if line[-1] == line[0]:
    s += int(line[-1])

print(s)