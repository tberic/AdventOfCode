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

def findHorizontalSymmetry(grid):
    m = len(grid)
    for y in range(1, m):
        found = True
        for i in range( min(y, m - y) ):
            if grid[y - i - 1] != grid[y + i]:
                found = False
                break
        if found:
            # print(y)
            return y

    return -1

f = open('input.txt', 'r')

lines = [line.strip() for line in f]
lines.append("")

notes = 0
for line in lines:
    if line == "":
        m = len(grid)
        n = len(grid[0])
        
        axis = findHorizontalSymmetry(grid)
        if axis == -1:
            grid = transpose(grid)
            axis = findHorizontalSymmetry(grid)
            if axis == -1:
                print('Error')
                grid = transpose(grid)
                printArray(grid)
            else:
                notes +=  axis
        else:
            notes += 100 * axis

        grid = []
    else:
        grid.append(line)


print(notes)