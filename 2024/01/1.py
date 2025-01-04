f = open('input.txt')

A = []
B = []

for line in f:
    a, b = list(map(int, line.strip().split('   ')))
    # print(s)
    # a, b = line.strip().split(' '), int)
    A.append(a)
    B.append(b)

A.sort()
B.sort()

distance = 0
for a, b in zip(A, B):
    distance += abs(a - b)

print(distance)