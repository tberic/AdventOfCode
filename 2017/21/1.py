def printMatrix(A):
    for i in range(len(A)):
        for j in range(len(A[i])):
            print(A[i][j], end='')
        print()

def flatten(A):
    B = ""
    for row in A:
        B += "".join(row)
        B += "/"
    return B[:-1]

def blowUp(a):
    A = []
    pos1 = 0
    pos2 = a.find("/")
    while pos2 != -1:
        A.append( list(a[pos1:pos2]) )
        pos1 = pos2+1
        pos2 = a.find("/", pos1)
    A.append( list(a[pos1:]) )
    return A

def transpose(A):
    B = [ [ A[j][i] for j in range(len(A))] for i in range(len(A)) ]
    return B

def hflip(A):
    B = [ A[len(A)-i-1][:] for i in range(len(A)) ]
    return B

def rotate(A):
    return hflip(transpose(A))

def square2to3(A):
    global rule2
    if flatten(A) in rule2:
        return blowUp(rule2[flatten(A)])    
    return None

def square3to4(A):
    global rule3
    if flatten(A) in rule3:
        return blowUp(rule3[flatten(A)])
    return None

rule2 = {}
rule3 = {}
f = open('input.txt', 'r')
for line in f:
    a, b = line.strip().split(' => ')
    if len(a) == 5:
        rule2[a] = b
        #generate all the other rules
        A = blowUp(a)
        for k in range(4):
            A = rotate(A)
            rule2[flatten(A)] = b
        A = hflip(A)
        rule2[flatten(A)] = b
        for k in range(4):
            A = rotate(A)
            rule2[flatten(A)] = b
    else:
        rule3[a] = b
        #generate all the other rules
        A = blowUp(a)
        for k in range(4):
            A = rotate(A)
            rule3[flatten(A)] = b
        A = hflip(A)
        rule3[flatten(A)] = b
        for k in range(4):
            A = rotate(A)
            rule3[flatten(A)] = b
f.close()

grid = [ list(".#."), list("..#"), list("###")]

for step in range(18):

    if len(grid) % 2 == 0:
        gridNew = [['.' for j in range(3*len(grid)//2)] for i in range(3*len(grid)//2)]

        for i in range(len(grid)//2):            
            for j in range(len(grid)//2):
                square2 = []
                square2.append( grid[2*i][ 2*j:2*j+2 ] )
                square2.append( grid[2*i+1][ 2*j:2*j+2 ] )

                square3 = square2to3(square2)
                for x in range(3):
                    for y in range(3):
                        gridNew[3*i+x][3*j+y] = square3[x][y]

        grid = [row[:] for row in gridNew]

    elif len(grid) % 3 == 0:
        gridNew = [['.' for j in range(4*len(grid)//3)] for i in range(4*len(grid)//3)]

        for i in range(len(grid)//3):            
            for j in range(len(grid)//3):
                square3 = []
                square3.append( grid[3*i][ 3*j:3*j+3 ] )
                square3.append( grid[3*i+1][ 3*j:3*j+3 ] )
                square3.append( grid[3*i+2][ 3*j:3*j+3 ] )
                
                square4 = square3to4(square3)
                for x in range(4):
                    for y in range(4):
                        gridNew[4*i+x][4*j+y] = square4[x][y]

        grid = [row[:] for row in gridNew]


count = 0
for i in range(len(grid)):
    for j in range(len(grid)):
        if grid[i][j] == '#':
            count += 1
print(count)