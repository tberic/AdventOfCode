from aoc import *

f = open('input.txt', 'r')
grid = [line.strip() for line in f]

startY, startX = 0, 0
for i, line in enumerate(grid):
    if 'S' in line:
        startY = i
        startX = line.index('S')
        break

visited = [[-1 for j in range(len(grid[0]))] for i in range(len(grid))]
Q = [(startY, startX, 0)]

STEPS_FINISHED = 131

while Q:
    y, x, steps = Q.pop(0)
    # print(y, x, steps)

    if y < 0 or x < 0:
        continue
    if y > len(grid) - 1 or x > len(grid[0]) - 1:
        continue

    if grid[y][x] == '#':
        continue

    if visited[y][x] != -1:
        continue

    visited[y][x] = steps

    if steps > STEPS_FINISHED:
        continue

    Q.append( (y-1, x, steps+1) )
    Q.append( (y+1, x, steps+1) )
    Q.append( (y, x-1, steps+1) )
    Q.append( (y, x+1, steps+1) )

# print(visited)
    
even_corners = 0
odd_corners = 0
evens = 0
odds = 0
for y in range(len(grid)):
    for x in range(len(grid[0])):
        if visited[y][x] >= 0:
            if visited[y][x] % 2 == 0:
                evens += 1
                if visited[y][x] > 65:
                    even_corners += 1
            else:
                odds += 1
                if visited[y][x] > 65:
                    odd_corners += 1

print(evens)
print(odds)
print(even_corners)
print(odd_corners)

n = (26501365 - 65) // 131

total = (n + 1)*(n + 1) * odds + n * n * evens - (n + 1) *  odd_corners + n * even_corners
print(total)