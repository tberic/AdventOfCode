import re
import heapq

f = open('input.txt', 'r')

before = {}
available = set([chr(i+65) for i in range(26)])

for line in f:
    m = re.match(r'Step (.+) must be finished before step (.+) can begin.', line.strip())
    a, b = m.groups()
    available.discard(b)
    if b in before:
        before[b].append(a)
    else:
        before[b] = [a]
f.close()

available = list(available)
heapq.heapify(available)

path = ""
while available:
    a = heapq.heappop(available)
    path += a

    for b in before:
        if b not in path and b not in available:
            t = 1
            for a in before[b]:
                if a not in path:
                    t = 0
                    break
            if t == 1:
                heapq.heappush(available, b)

print(path)