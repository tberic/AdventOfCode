fin = open('input.txt', 'r')

grid = [list(map(int, list(line.strip()))) for line in fin]

visible = [[0 for j in range(len(grid[0]))] for i in range(len(grid))]

# look from the left side
for i in range(len(grid)):
    highest = -1
    for j in range(len(grid[i])):
        if grid[i][j] > highest:
            visible[i][j] = 1
            highest = grid[i][j]

# look from the right side
for i in range(len(grid)):
    highest = -1
    for j in range(len(grid[0])-1, -1, -1):
        if grid[i][j] > highest:
            visible[i][j] = 1
            highest = grid[i][j]

# look from the top side
for j in range(len(grid[0])):
    highest = -1
    for i in range(len(grid)):
        if grid[i][j] > highest:
            visible[i][j] = 1
            highest = grid[i][j]

# look from the bottom side
for j in range(len(grid[0])):
    highest = -1
    for i in range(len(grid)-1, -1, -1):
        if grid[i][j] > highest:
            visible[i][j] = 1
            highest = grid[i][j]

# print(visible)

print(sum(sum(visible, [])))