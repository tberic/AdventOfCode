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
    [5, 7, 6, 1, 4],
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

def FloydWarshall(dist):
    for i1 in range(4):
        for j1 in range(3):
            for i2 in range(4):
                for j2 in range(3):
                    for i3 in range(4):
                        for j3 in range(3):
                            if dist[((i1, j1), (i2, j2))] > dist[((i1, j1), (i3, j3))] + dist[((i3, j3), (i2, j2))]:
                                dist[((i1, j1), (i2, j2))] = dist[((i1, j1), (i3, j3))] + dist[((i3, j3), (i2, j2))]

def outOfBounds(y, x):
    if y < 0 or x < 0:
        return True
    if y >= 4 or x >= 3:
        return True
    return False

def BFS(y1, x1, dist_arr, last_state):
    dist_arr[y][x] = 0

    Q = []
    Q.append([y, x, ENTER])
    while Q:
        y, x, state = Q.pop(0)

        if GRID[y][x] == '#':
            continue
        
        for new_state, dir in enumerate(DIRS):
            if outOfBounds(y + dir[0], x + dir[1]):
                continue
            if dist_arr[y + dir[0]][x + dir[1]] > dist_arr[y][x] + TRANSITION_MATRIX[state][new_state] and GRID[y + dir[0]][x + dir[1]] != '#':
                Q.append([y + dir[0], x + dir[1], new_state])
                dist_arr[y + dir[0]][x + dir[1]] = dist_arr[y][x] + TRANSITION_MATRIX[state][new_state]
                last_state[y + dir[0]][x + dir[1]] = new_state


f = open('input0.txt')

dist = {
    ((i1, j1), (i2, j2)) : 10 ** 10
    for j1 in range(3) for i1 in range(4) for j2 in range(3) for i2 in range(4)
}
for y in range(4):
    for x in range(3):
        dist[((y, x), (y, x))] = 0

        dist_from_source = [[10 ** 10 for j in range(3)] for i in range(4)]
        states = [[0 for j in range(3)] for i in range(4)]
        BFS(y, x, dist_from_source, states)
        for yy in range(4):
            for xx in range(3):
                dist[( (y, x), (yy, xx) )] = dist_from_source[yy][xx] + TRANSITION_MATRIX[states[yy][xx]][ENTER]

# print(dist)
# print(dist[( (0, 2), (3, 2) )])

total = 0
for line in f:
    code = line.strip()

    steps = dist[ (find('A'), find(code[0])) ]
    for i in range(len(code) - 1):
        print(code[i], code[i+1])
        steps += dist[ (find(code[i]), find(code[i+1])) ]

    print(steps)
    total += steps * int(code[:-1])
    # print(steps * int(code[:-1]))

print(total)