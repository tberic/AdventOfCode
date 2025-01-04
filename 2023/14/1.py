def printArray(A):
    for row in A:
        print("".join(row))
    print()
    print()


f = open('input.txt', 'r')

grid = [list(line.strip()) for line in f]

for y in range(len(grid)):
    for x in range(len(grid[0])):
        if grid[y][x] == 'O':
            yy = y
            while yy > 0:
                yy -= 1
                if grid[yy][x] in ['#', 'O']:
                    yy += 1
                    break

            grid[y][x] = '.'
            grid[yy][x] = 'O'

# printArray(grid)

sum = 0
n = len(grid)
for y in range(len(grid)):
    for x in range(len(grid[0])):
        if grid[y][x] == 'O':
            sum += n-y

print(sum)