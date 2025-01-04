def outOfBounds(x, y):
    if x < 0 or y < 0:
        return True
    if x >= len(grid):
        return True
    if y >= len(grid[0]):
        return True
    return False

def search(x, y, text, dir):
    if text == "":
        return True
    if outOfBounds(x, y):
        return False
    if text[0] != grid[x][y]:
        return False
    return search(x + dir[0], y + dir[1], text[1:], dir)

dirs = [
    [-1, -1],
    [-1, 0],
    [-1, +1],
    [0, -1],
    [0, +1],
    [+1, -1],
    [+1, 0],
    [+1, +1]    
]

f = open('input.txt')
grid = [line.strip() for line in f]

total = 0
for x in range(len(grid)):
    for y in range(len(grid[x])):
        for dir in dirs:
            if search(x, y, 'XMAS', dir):
                total += 1

print(total)