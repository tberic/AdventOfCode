import re

def left(t, i):
    global speed, time, rest
    if t >= time[i]:
        return speed[i]*time[i]
    return speed[i]*t

name = {}
speed = [0 for i in range(9)]
time = [0 for i in range(9)]
rest = [0 for i in range(9)]

f = open('input.txt', 'r')
n = 0
for line in f:
    m = re.search(r'(.*) can fly (\d+) km/s for (\d+) seconds, but then must rest for (\d+) seconds\.', line)
    a, v, t, r = m.groups()
    if a not in name:
        name[a] = n
        n += 1
    speed[name[a]] = int(v)
    time[name[a]] = int(t)
    rest[name[a]] = int(r)
f.close()

#print(speed)
#print(time)
#print(rest)

T = 2503
dist = [0 for i in range(n)]
for i in range(n):
    dist[i] = T//(time[i] + rest[i])*speed[i]*time[i] + left(T%(time[i] + rest[i]), i)

dist.sort()
print(dist[-1])