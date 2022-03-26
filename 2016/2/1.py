def check(i, j):
    if i < 0 or i > 2:
        return False
    if j < 0 or j > 2:
        return False
    return True

f = open('input.txt', 'r')

keypad = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
move = { 'U': (-1, 0), 'D': (+1, 0), 'L': (0, -1), 'R': (0, +1) }

x, y = (1, 1)
for line in f:
    for c in line.strip():
        if check(x + move[c][0], y + move[c][1]):
            x = x + move[c][0]
            y = y + move[c][1]

    print(keypad[x][y])

f.close()