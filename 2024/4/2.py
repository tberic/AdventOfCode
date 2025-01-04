def search(x, y, pattern):
    for i in range(len(pattern)):
        for j in range(len(pattern[0])):
            if pattern[i][j] == '.':
                continue
            if pattern[i][j] != grid[x + i][y + j]:
                return False
    return True

patterns = [
    ['M.S', '.A.', 'M.S'],
    ['S.S', '.A.', 'M.M'],
    ['M.M', '.A.', 'S.S'],
    ['S.M', '.A.', 'S.M'],
]

f = open('input.txt')
grid = [line.strip() for line in f]

total = 0
for x in range(len(grid) - 2):
    for y in range(len(grid[x]) - 2):
        for pattern in patterns:
            if search(x, y, pattern):
                total += 1

print(total)