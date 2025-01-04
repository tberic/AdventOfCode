grid = []

def isdigit(c):
    return (c >= '0' and c <= '9')

def isDigit(x, y):
    return isdigit(grid[x][y])

def issymbol(c):
    return (c != '.' and not isdigit(c))

def isSymbol(x, y):
    return issymbol(grid[x][y])

def partDigit(x, y):
    if (not isDigit(x, y)):
        return False
    return isSymbol(x-1, y-1) or isSymbol(x-1, y) or isSymbol(x-1, y+1) or \
           isSymbol(x, y-1) or                       isSymbol(x, y+1) or \
           isSymbol(x+1, y-1) or isSymbol(x+1, y) or isSymbol(x+1, y+1)

f = open('input.txt', 'r')

sumPartNumber = 0

for line in f:
    grid.append('..' + line.strip() + '..')
grid.append('.' * len(grid[0]))
grid.append('.' * len(grid[0]))
grid = ['.' * len(grid[0])] + grid
grid = ['.' * len(grid[0])] + grid

num = ""
partNumber = False
for x in range(1, len(grid)-1):
    for y in range(1, len(grid[x])-1):
        if (isDigit(x, y)):
            num += grid[x][y]
            if (partDigit(x, y)):
                partNumber = True
        if (grid[x][y] == '.' or isSymbol(x, y)):
            if (num != "" and partNumber):
                sumPartNumber += int(num)
            partNumber = False
            num = ""
    
print(sumPartNumber)

# for x in range(len(grid)):
#     for y in range(len(grid[x])):
#         print(grid[x][y], end='')
#     print()

