import re

f = open('input.txt', 'r')
log = []
for line in f:
    m = re.match(r'\[(\d+)\-(\d+)\-(\d+) (\d+):(\d+)\] (.+)', line.strip())
    y, m, d, h, min, msg = m.groups()
    log.append( (int(y), int(m), int(d), int(h), int(min), msg) )    
f.close()

log = sorted(log)

ID = 0
asleep = {}
for y, m, d, h, min, msg in log:
    if msg == "falls asleep":
        asleepStart = min
    elif msg == "wakes up":
        asleepEnd = min
        mins = [0 for i in range(60)]
        for i in range(asleepStart, asleepEnd):
            mins[i] = 1
        if ID not in asleep:
            asleep[ID] = list(mins)
        else:
            for i in range(60):
                asleep[ID][i] += mins[i]
    else:
        m = re.match(r'Guard #(\d+) begins shift', msg)
        ID = int(m.group(1))

maxMins = 0
maxID = 0
for ID, seq in asleep.items():
    if sum(seq) > maxMins:
        maxMins = sum(seq)
        maxID = ID

m = max(asleep[maxID])
print(maxID*asleep[maxID].index(m))