import re
import itertools

name = {}
rel = [[0 for i in range(8)] for j in range(8)]

f = open('input.txt', 'r')
n = 0
for line in f:
    m = re.search(r'(.*) would (.*) (\d+) happiness units by sitting next to (.*)\.', line)
    a, mood, x, b = m.groups()
    if a not in name:
        name[a] = n
        n += 1
    if b not in name:
        name[b] = n
        n += 1
    points = int(x)
    if mood == "lose":
        points = -points
    rel[name[a]][name[b]] = points
f.close()

max = 0
for p in itertools.permutations(range(n)):
    sum = 0
    for i in range(len(p)):
        sum += rel[ p[i] ][ p[(i-1)%n] ] + rel[ p[i] ][ p[(i+1)%n] ]
    
    if sum > max:
        max = sum

print(max)