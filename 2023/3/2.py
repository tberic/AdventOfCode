grid = []

def isdigit(c):
    return (c >= '0' and c <= '9')

def isDigit(x, y):
    return isdigit(grid[x][y])

def issymbol(c):
    return (c != '.' and not isdigit(c))

def isSymbol(x, y):
    return issymbol(grid[x][y])

def findNum(x, y):
    a = y
    while (isDigit(x, a)):
        a -= 1
    a += 1
    b = y
    while (isDigit(x, b)):
        b += 1

    return int(grid[x][a:b])

def isGear(x, y):
    if (grid[x][y] != '*'):
        return 0
    nums = 0
    nums += isDigit(x, y-1)
    nums += isDigit(x, y+1)
    if (not isDigit(x-1, y)):
        nums += isDigit(x-1, y-1)
        nums += isDigit(x-1, y+1)
    else:
        nums += 1
    if (not isDigit(x+1, y)):
        nums += isDigit(x+1, y-1)
        nums += isDigit(x+1, y+1)
    else:
        nums += 1
    
    if nums != 2:
        return 0

    gearRatio = 1
    if isDigit(x, y-1):
        gearRatio *= findNum(x, y-1)
    if isDigit(x, y+1):
        gearRatio *= findNum(x, y+1)

    if not isDigit(x-1, y):
        if isDigit(x-1, y-1):
            gearRatio *= findNum(x-1, y-1)
        if isDigit(x-1, y+1):
            gearRatio *= findNum(x-1, y+1)
    if isDigit(x-1, y):
        gearRatio *= findNum(x-1, y)
    
    if not isDigit(x+1, y):
        if isDigit(x+1, y-1):
            gearRatio *= findNum(x+1, y-1)
        if isDigit(x+1, y+1):
            gearRatio *= findNum(x+1, y+1)
    if isDigit(x+1, y):
        gearRatio *= findNum(x+1, y)

    return gearRatio

f = open('input.txt', 'r')

sumPartNumber = 0

for line in f:
    grid.append('..' + line.strip() + '..')
grid.append('.' * len(grid[0]))
grid.append('.' * len(grid[0]))
grid = ['.' * len(grid[0])] + grid
grid = ['.' * len(grid[0])] + grid

sumGears = 0
for x in range(1, len(grid)-1):
    for y in range(1, len(grid[x])-1):
        sumGears += isGear(x, y)
        
print(sumGears)

# for x in range(len(grid)):
#     for y in range(len(grid[x])):
#         if isGear(x, y):
#             print('_', end='')
#         else:
#             print(grid[x][y], end='')
#     print()

