from itertools import combinations

f = open('input.txt', 'r')
s = 0
for line in f:
    a = list(map(int, line.strip().split()))
    for x, y in combinations(a, 2):
            if x % y == 0:
                s += x // y
                break
            elif y % x == 0:
                s += y // x
                break

f.close()

print(s)