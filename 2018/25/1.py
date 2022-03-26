import re

def dist(A, B):
    return abs(A[0]-B[0]) + abs(A[1]-B[1]) + abs(A[2]-B[2]) + abs(A[3]-B[3])


def inside(T, c):
    for X in c:
        if dist(T, X) <= 3:
            return True
    return False


def close(a, b):
    for T1 in a:
        for T2 in b:
            if dist(T1, T2) <= 3:
                return True
    return False


points = []
constellations = []

f = open('input.txt', 'r')

for line in f:
    points.append(tuple(map(int, line.strip().split(','))))

    l = []
    for i in range(len(constellations)-1, -1, -1):
        if inside(points[-1], constellations[i]):
            l.append(i)

    if l:
        newConstellation = []
        for i in l:
            newConstellation += constellations[i]
        newConstellation.append(points[-1])
        for i in l:
            constellations.pop(i)
        constellations.append(newConstellation)
    else:
        constellations.append([points[-1]])

f.close()

#points.sort(key=lambda x: dist(x, (0,0,0,0)))

# consolidate the constellations


i = len(constellations)-1
while i >= 0:
    j = i-1
    while j >= 0:
        if close(constellations[i], constellations[j]):
            constellations[j] += constellations[i]
            constellations.pop(i)
            i -= 1
            break
        j -= 1
    i -= 1

print(constellations)
print(len(constellations))
