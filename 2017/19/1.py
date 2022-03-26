f = open('input.txt', 'r')
grid = [[' '] + [c for c in line[:-1]] + [' '] for line in f]
f.close()

x = "".join(grid[0]).find('|')
y = 0
dir = [+1, 0]

path = ""
steps = 0

while grid[y][x] != ' ':
    steps += 1
    #print(y, x)

    if grid[y][x].isalpha():
        path += grid[y][x]

    if grid[y][x] == '|':
        pass        
    if grid[y][x] == '-':
        pass
    if grid[y][x] == '+':
        if grid[y+dir[0]][x+dir[1]] == ' ':
            if dir[0]:
                if grid[y][x-1] != ' ':
                    dir = [0, -1]
                elif grid[y][x+1] != ' ':
                    dir = [0, +1]
            elif dir[1]:
                if grid[y-1][x] != ' ':
                    dir = [-1, 0]
                elif grid[y+1][x] != ' ':
                    dir = [+1, 0]

    y += dir[0]
    x += dir[1]


print(path)
print(steps)