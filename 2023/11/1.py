def printArray(A):
    for row in A:
        print("".join(row))
    print()
    print()

def transpose(A):
    B = [['.' for j in range(len(A))] for i in range(len(A[0]))]
    for i in range(len(A)):
        for j in range(len(A[0])):
            B[j][i] = A[i][j]
    return B


def dist(A, B):
    return abs(A[0] - B[0]) + abs(A[1] - B[1])

def expandRows(A):
    B = []
    for row in A:
        B.append(row)
        if not '#' in row:
            B.append(row)
    return B


f = open('input.txt', 'r')

universe = [line.strip() for line in f]

# expand universe - expand rows and expand columns
universe = expandRows(universe)
universe = transpose(universe)
universe = expandRows(universe)
universe = transpose(universe)

# printArray(universe)

# find galaxies

galaxies = []
for y in range(len(universe)):
    for x in range(len(universe[0])):
        if universe[y][x] == '#':
            galaxies.append( (y, x) )

sum = 0
for i in range(len(galaxies)):
    for j in range(i+1, len(galaxies)):
        sum += dist( galaxies[i], galaxies[j] )

print(sum)