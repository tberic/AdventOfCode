def outOfBounds(x, y):
    if x < 0 or y < 0:
        return True
    if x >= len(grid):
        return True
    if y >= len(grid[0]):
        return True
    return False

f = open('input.txt')

grid = [line.strip() for line in f]

antennae = {}
for x in range(len(grid)):
    for y in range(len(grid[0])):
        if grid[x][y] != '.':
            freq = grid[x][y]
            if freq not in antennae:
                antennae[ freq ] = [ (x, y) ]
            else:
                antennae[ freq ].append( (x, y) )

antinodes = [[0 for j in range(len(grid[0]))] for i in range(len(grid))]
for freq in antennae:
    for i in range(len(antennae[freq])):
        for j in range(i+1, len(antennae[freq])):
            dx = antennae[freq][i][0] - antennae[freq][j][0]
            dy = antennae[freq][i][1] - antennae[freq][j][1]

            x = antennae[freq][i][0]
            y = antennae[freq][i][1]
            while True:
                antinodes[x][y] = 1
                x = x + dx
                y = y + dy

                if outOfBounds(x, y):
                    break

            x = antennae[freq][j][0]
            y = antennae[freq][j][1]
            while True:
                antinodes[x][y] = 1                
                x = x - dx
                y = y - dy

                if outOfBounds(x, y):
                    break                

total = 0
for i in  range(len(antinodes)):
    for j in  range(len(antinodes[0])):
        total += antinodes[i][j]
print(total)