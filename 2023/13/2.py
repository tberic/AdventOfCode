grid = []

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

def flipBit(c):
    if c == '.':
        return '#'
    if c == '#':
        return '.'
    print('bitFlip: Error')

def compare(A, B):
    cnt = 0
    for i in range(len(A)):
        if A[i] != B[i]:
            cnt += 1
    return cnt

def findHorizontalSymmetry(grid):
    m = len(grid)
    for y in range(1, m):
        diffs = 0
        for i in range( min(y, m - y) ):
            diffs += compare(grid[y - i - 1], grid[y + i])
        if diffs == 1:
            return y

    return None

def findVerticalSymmetry(grid):
    return findHorizontalSymmetry(transpose(grid))


f = open('input.txt', 'r')

lines = [line.strip() for line in f]
lines.append("")

notes = 0
for line in lines:
    if line == "":
        axis = findHorizontalSymmetry(grid)
        if not axis:
            axis = findVerticalSymmetry(grid)
            if not axis:
                pass
            else:
                notes += axis
        else:
            notes += 100 * axis

        grid = []
        print(notes)
    else:
        grid.append(list(line))


print(notes)