import re
f = open('input.txt', 'r')

grid = [[0 for i in range(1000)] for j in range(1000)]

for line in f:
    m = re.search(r'(.*) (\d+),(\d+) through (\d+),(\d+)', line)
    command, x1, y1, x2, y2 = m.groups()    
    x1, y1, x2, y2 = list(map(int, [x1, y1, x2, y2]))
    if command == "turn on":
        for x in range(x1, x2+1):
            for y in range(y1, y2+1):
                grid[x][y] += 1
    elif command == "turn off":
        for x in range(x1, x2+1):
            for y in range(y1, y2+1):
                if grid[x][y]:
                    grid[x][y] -= 1
    elif command == "toggle":
        for x in range(x1, x2+1):
            for y in range(y1, y2+1):
                grid[x][y] += 2


count = 0
for x in range(1000):
    for y in range(1000):
        count += grid[x][y]
print(count)


f.close()