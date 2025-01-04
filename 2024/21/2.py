from copy import deepcopy
from functools import lru_cache

@lru_cache
def transition(state1, state2, depth):
    if depth == 1:
        return len(TRANSITIONS[state1][state2][0])
    
    best = 10 ** 30
    for possibility in TRANSITIONS[state1][state2]:
        length = 0
        path = [ENTER] + possibility
        for i in range(len(path) - 1):
            length += transition(path[i], path[i+1], depth-1)
        
        if length < best:
            best = length
        
    return best

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

TRANSITIONS = [
    [[ [ENTER] ], [ [RIGHT, RIGHT, ENTER] ], [ [RIGHT, ENTER] ], [ [RIGHT, UP, ENTER] ], [[RIGHT, RIGHT, UP, ENTER], [RIGHT, UP, RIGHT, ENTER]] ],
    [[ [LEFT, LEFT, ENTER] ], [ [ENTER] ], [ [LEFT, ENTER] ], [ [LEFT, UP, ENTER], [UP, LEFT, ENTER] ], [ [UP, ENTER] ]],
    [[ [LEFT, ENTER] ], [ [RIGHT, ENTER] ], [ [ENTER] ], [ [UP, ENTER] ], [ [RIGHT, UP, ENTER], [UP, RIGHT, ENTER] ]],
    [[ [DOWN, LEFT, ENTER] ], [ [DOWN, RIGHT, ENTER], [RIGHT, DOWN, ENTER] ], [ [DOWN, ENTER] ], [ [ENTER] ], [ [RIGHT, ENTER] ]],
    [[ [DOWN, LEFT, LEFT, ENTER], [LEFT, DOWN, LEFT, ENTER] ], [ [DOWN, ENTER] ], [ [DOWN, LEFT, ENTER], [LEFT, DOWN, ENTER] ], [ [LEFT, ENTER] ], [ [ENTER] ]],
]

TRANSITION_MATRIX = [[0 for j in range(5)] for i in range(5)]

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
    Q.append([0, y1, x1, ENTER])
    best = 10 ** 30

    visited = [[0 for j in range(3)] for i in range(4)]
    while Q:
        steps, y, x, state = Q.pop(0)

        if outOfBounds(y, x):
            continue

        if GRID[y][x] == '#':
            continue

        if y == y2 and x == x2:
            if steps + TRANSITION_MATRIX[state][ENTER] < best:
                best = steps + TRANSITION_MATRIX[state][ENTER]
            continue

        if visited[y][x] & (2 ** state):
            continue
        visited[y][x] |= 2 ** state
        
        for new_state, dir in enumerate(DIRS):
            Q.append([steps + TRANSITION_MATRIX[state][new_state],y + dir[0], x + dir[1], new_state])
    
    return best


f = open('input.txt')

DEPTH = 25
for i in range(5):
    for j in range(5):
        TRANSITION_MATRIX[i][j] = transition(i, j, DEPTH)
print(TRANSITION_MATRIX)

total = 0
for line in f:
    code = line.strip()

    steps = BFS( find('A'), find(code[0]) )
    for i in range(len(code) - 1):
        dist = BFS( find(code[i]), find(code[i+1]) )
        # print(code[i], code[i+1], dist)
        steps += dist

    print(steps, int(code[:-1]))
    total += steps * int(code[:-1])

print(total)