import re
import heapq

f = open('input.txt', 'r')

nLetters = 26
before = {}
available = set([chr(i+65) for i in range(nLetters)])

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
t = 0
worker = {}
nWorkers = 5
while len(path) < nLetters:
    for a in list(worker.keys()):
        worker[a] -= 1
        if worker[a] == 0:
            path += a            
            del worker[a]

    for b in before:
        if b not in path and b not in available and b not in worker:
            flag = 1
            for a in before[b]:
                if a not in path:
                    flag = 0
                    break
            if flag == 1:
                heapq.heappush(available, b)

    while len(worker) < nWorkers and available:
        a = heapq.heappop(available)
        worker[a] = 61 + ord(a)-65

    #print(t, worker)

    t += 1

print(path)
print(t-1)