f = open('input.txt', 'r')
line = f.readline().strip()
f.close()

s = 0
n = len(line)
for i in range(n):
    if line[i] == line[(i+n//2) % n]:
        s += int(line[i])
print(s)