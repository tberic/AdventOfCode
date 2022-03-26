import re

f = open('input.txt', 'r')

count = 0
for s in f:
    line = s.strip()
    a = line.count('a')
    e = line.count('e')
    i = line.count('i')
    o = line.count('o')
    u = line.count('u')
    if (a+e+i+o+u < 3):
        continue
    if ('ab' in line) or ('cd' in line) or ('pq' in line) or ('xy' in line):
        continue
    m = re.search(r'(\w)\1', line)
    if not m:
        continue

    count += 1

print(count)

f.close()