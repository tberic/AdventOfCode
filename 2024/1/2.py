f = open('input.txt')

A = []
B = []

for line in f:
    a, b = list(map(int, line.strip().split('   ')))
    A.append(a)
    B.append(b)

similarity = 0
for a in A:    
    similarity += a * B.count(a)

print(similarity)