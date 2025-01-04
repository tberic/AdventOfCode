import re

def overlaps(A, B):
    if (A[2] < B[0] or A[2] > B[2]) and (B[2] < A[0] or B[2] > A[2]):
        return False
    if (A[3] < B[1] or A[3] > B[3]) and (B[3] < A[1] or B[3] > A[3]):
        return False

    return True

f = open('input.txt', 'r')

rect = []
for line in f:
    m = re.match(r'#(\d+) @ (\d+),(\d+): (\d+)x(\d+)', line.strip())
    id, x, y, a, b = list(map(int, m.groups()))
    rect.append( (x, y, x+a, y+b) )
f.close()

for i in range(len(rect)):
    overlap = 0
    for j in range(len(rect)):
        if i != j and overlaps(rect[i], rect[j]):
            overlap = 1
            break
    if overlap == 0:
        print(i+1)
        break