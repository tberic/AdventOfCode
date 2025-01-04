OFFSET = 10 ** 6

def transpose(A):
    B = [['.' for j in range(len(A))] for i in range(len(A[0]))]
    for i in range(len(A)):
        for j in range(len(A[0])):
            B[j][i] = A[i][j]
    return B

def dist(A, B):
    return abs(A[0] - B[0]) + abs(A[1] - B[1]) + \
        abs(rowOffset[A[0]] - rowOffset[B[0]]) * (OFFSET-1) + \
        abs(colOffset[A[1]] - colOffset[B[1]]) * (OFFSET-1)

def countLess(A, x):
    count = 0
    for a in A:
        if a < x:
            count += 1
    return count

f = open('input.txt', 'r')

universe = [line.strip() for line in f]

# find galaxies
galaxies = []
for y in range(len(universe)):
    for x in range(len(universe[0])):
        if universe[y][x] == '#':
            galaxies.append( (y, x) )

# find empty rows
emptyRows = []
for i, row in enumerate(universe):
    if '#' not in row:
        emptyRows.append(i)
print(emptyRows)

# find empty columns
emptyCols = []
universe = transpose(universe)
for i, col in enumerate(universe):
    if '#' not in col:
        emptyCols.append(i)
print(emptyCols)

rowOffset = [0 for i in range(len(universe[0]))]
for i in range(len(universe[0])):
    rowOffset[i] += countLess(emptyRows, i)

print(rowOffset)

colOffset = [0 for i in range(len(universe))]
for i in range(len(universe)):
    colOffset[i] += countLess(emptyCols, i)

print(colOffset)

sum = 0
for i in range(len(galaxies)):
    for j in range(i+1, len(galaxies)):
        sum += dist( galaxies[i], galaxies[j] )

print(sum)