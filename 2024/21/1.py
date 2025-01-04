LEFT = 0
RIGHT = 1
DOWN = 2
UP = 3
ENTER = 4

DIRS = [
    [0, -1],
    [0, +1],
    [+1, 0],
    [-1, 0],
]

TRANSITION_MATRIX = [
    [1, 5, 4, 7, 8],
    [9, 1, 8, 9, 4],
    [8, 4, 1, 4, 7],
    [9, 7, 6, 1, 4],
    [10, 6, 9, 8, 1],
]

GRID = [
    "789",
    "456",
    "123",
    "#0A",
]

def find(chr):
    for i, s in enumerate(GRID):
        if chr in s:
            y = i
    x = GRID[y].find(chr)
    return (y, x)

def outOfBounds(y, x):
    if y < 0 or x < 0:
        return True
    if y >= 4 or x >= 3:
        return True
    return False

def BFS(point1, point2):
    Q = []
    y1, x1 = point1
    y2, x2 = point2
    Q.append([0, y1, x1, ENTER, []])
    best = 10 ** 10

    visited = [[0 for j in range(3)] for i in range(4)]
    while Q:
        steps, y, x, state, path = Q.pop(0)

        if outOfBounds(y, x):
            continue

        if GRID[y][x] == '#':
            continue

        if y == y2 and x == x2:
            print(path)
            if steps + TRANSITION_MATRIX[state][ENTER] < best:
                best = steps + TRANSITION_MATRIX[state][ENTER]
            continue

        if visited[y][x] & (2 ** state):
            continue
        visited[y][x] |= 2 ** state
        
        for new_state, dir in enumerate(DIRS):
            Q.append([steps + TRANSITION_MATRIX[state][new_state],y + dir[0], x + dir[1], new_state, path+[new_state]])
    
    return best


f = open('input.txt')

# print(BFS( find('A'), find('1') ))

total = 0
for line in f:
    code = line.strip()

    steps = BFS( find('A'), find(code[0]) )
    print('A', code[0], steps)
    for i in range(len(code) - 1):
        dist = BFS( find(code[i]), find(code[i+1]) )
        print(code[i], code[i+1], dist)
        steps += dist

    print(steps)
    total += steps * int(code[:-1])
    # print(steps * int(code[:-1]))

print(total)