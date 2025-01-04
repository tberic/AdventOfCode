def walk(y, x):

    steps = 0
    while True:
        steps += 1
        if visited[y][x]:
            return 0
        
        visited[y][x] = steps

        if grid[y][x] == '|':
            if y > 0 and not visited[y-1][x]:
                y = y-1
                continue
            if y < m and not visited[y+1][x]:
                y = y+1
                continue

        if grid[y][x] == '-':
            if x > 0 and not visited[y][x-1]:
                x = x-1
                continue
            if x < n and not visited[y][x+1]:
                x = x+1
                continue

        if grid[y][x] == 'L':
            if y > 0 and not visited[y-1][x]:
                y = y-1
                continue
            if x < n and not visited[y][x+1]:
                x = x+1
                continue

        if grid[y][x] == 'J':
            if y > 0 and not visited[y-1][x]:
                y = y-1
                continue
            if x > 0 and not visited[y][x-1]:
                x = x-1
                continue

        if grid[y][x] == '7':
            if x > 0 and not visited[y][x-1]:
                x = x-1
                continue
            if y < m and not visited[y+1][x]:
                y = y+1
                continue

        if grid[y][x] == 'F':
            if x < n and not visited[y][x+1]:
                x = x+1
                continue
            if y < m and not visited[y+1][x]:
                y = y+1
                continue

f = open('input.txt', 'r')

grid = [line.strip() for line in f]
m = len(grid)
n = len(grid[0])
visited = [[0 for i in range(len(grid[0]))] for j in range(len(grid))]

for y in range(len(grid)):
    for x in range(len(grid[0])):
        if (grid[y][x] == 'S'):
            posX = x
            posY = y

visited[posY][posX] = -1

if grid[posY-1][posX] == '|' or grid[posY-1][posX] == '7' or grid[posY-1][posX] == 'F':
    walk(posY - 1, posX)
elif grid[posY+1][posX] == '|' or grid[posY+1][posX] == 'L' or grid[posY+1][posX] == 'J':
    walk(posY + 1, posX)
elif grid[posY][posX-1] == '-' or grid[posY][posX-1] == 'L' or grid[posY][posX-1] == 'F':
    walk(posY, posX - 1)
elif grid[posY][posX+1] == '-' or grid[posY][posX+1] == 'J' or grid[posY][posX+1] == '7':
    walk(posY, posX + 1)

# print(visited)

max = 0
for y in range(len(visited)):
    for x in range(len(visited[0])):
        if (visited[y][x] > max):
            max = visited[y][x]

print((max + 1) // 2)