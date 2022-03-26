f = open('input.txt', 'r')
grid = []
flashed = [[0 for i in range(10)] for j in range(10)]

for line in f:
        x = [int(i) for i in line[:-1]]
        grid.append(x)

def printMatrix(a):
        for i in range(10):
                for j in range(10):
                        print(a[i][j], end='')
                print()

def zeroOut(a):
        for i in range(10):
                for j in range(10):
                        a[i][j] = 0

def makeStep():
        for i in range(10):
                for j in range(10):
                        floodFill(i, j)

def floodFill(x, y):
        if (x < 0 or x > 9):
                return 
        if (y < 0 or y > 9):
                return 
        if (flashed[x][y]):
                return 
        if (grid[x][y] < 9):
                grid[x][y] += 1
        elif (grid[x][y] == 9):
                flashed[x][y] = 1
                grid[x][y] = 0
                floodFill(x-1, y-1)
                floodFill(x-1, y)
                floodFill(x-1, y+1)
                floodFill(x, y-1)
                floodFill(x, y+1)
                floodFill(x+1, y-1)
                floodFill(x+1, y)
                floodFill(x+1, y+1)
        

for step in range(10000): #simulate a 100 steps        
        zeroOut(flashed)
        makeStep()
        flashes = sum(sum(flashed,[]))
        if (flashes == 100):
            break
        #printMatrix(grid)

print(step+1)

f.close()