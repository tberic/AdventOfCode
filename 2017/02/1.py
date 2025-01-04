f = open('input.txt', 'r')
s = 0
for line in f:
    a = list(map(int, line.strip().split()))
    s += max(a) - min(a)
f.close()

print(s)