def check(i, j):
    if i == 0 and 0 <= j <= 4:
        return True
    if i == 1 and 1 <= j <= 3:
        return True
    if i == -1 and 1 <= j <= 3:
        return True
    if i == 2 and j == 2:
        return True
    if i == -2 and j == 2:
        return True
    return False

f = open('input.txt', 'r')

keypad = [['0', '0', '1', '0', '0'], 
          ['0', '2', '3', '4', '0'], 
          ['5', '6', '7', '8', '9'], 
          ['0', 'A', 'B', 'C', '0'], 
          ['0', '0', 'D', '0', '0']]
move = { 'U': (-1, 0), 'D': (+1, 0), 'L': (0, -1), 'R': (0, +1) }

x, y = (1, 1)
for line in f:
    for c in line.strip():
        if check(x + move[c][0], y + move[c][1]):
            x = x + move[c][0]
            y = y + move[c][1]

    print(keypad[x+2][y])

f.close()