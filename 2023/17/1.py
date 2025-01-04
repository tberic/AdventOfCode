from collections import defaultdict
import heapq

UP = (-1, 0)
DOWN = (+1, 0)
LEFT = (0, -1)
RIGHT = (0, +1)

def turnLeft(dir):
    if dir == UP:
        return LEFT
    if dir == DOWN:
        return RIGHT
    if dir == LEFT:
        return DOWN
    if dir == RIGHT:
        return UP
    print('Error: Turn left')

def turnRight(dir):
    if dir == UP:
        return RIGHT
    if dir == DOWN:
        return LEFT
    if dir == LEFT:
        return UP
    if dir == RIGHT:
        return DOWN
    print('Error: Turn right')

def dirIndex(dir):
    if dir == UP:
        return 0
    if dir == DOWN:
        return 1
    if dir == LEFT:
        return 2
    if dir == RIGHT:
        return 3
    print('Error: dirIndex')

def dirFromIndex(i):
    if i == 0:
        return UP
    if i == 1:
        return DOWN
    if i == 2:
        return LEFT
    if i == 3:
        return RIGHT
    print('Error: dirFromIndex')


f = open('input.txt', 'r')

grid = [list(map(int, list(line.strip()))) for line in f]
m = len(grid)
n = len(grid[0])

cost = defaultdict(lambda: 10 ** 10)

PQ = []
heapq.heappush(PQ, (0, 0, 0, 0, dirIndex(RIGHT)))
heapq.heappush(PQ, (0, 0, 0, 0, dirIndex(DOWN)))

minLoss = 10 ** 10
while PQ:
    heatLoss, y, x, straightLineRun, ind = heapq.heappop(PQ)
    dir = dirFromIndex(ind)

    if heatLoss >= cost[y, x, straightLineRun, ind]:
        continue

    cost[y, x, straightLineRun, ind] = heatLoss

    # print(y, x, heatLoss, straightLineRun, dir)

    if y == m-1 and x == n-1:
        print(heatLoss)
        break

    # keep going
    if straightLineRun < 3:
        yy, xx = y + dir[0], x + dir[1]
        if yy >= 0 and yy < m and xx >= 0 and xx < n:
            heapq.heappush(PQ, (heatLoss + grid[yy][xx], yy, xx, straightLineRun + 1, dirIndex(dir)))

    # go left
    dirL = turnLeft(dir)
    yy, xx = y + dirL[0], x + dirL[1]
    if yy >= 0 and yy < m and xx >= 0 and xx < n:
        heapq.heappush(PQ, (heatLoss + grid[yy][xx], yy, xx, 1, dirIndex(dirL)) )

    #go right
    dirR = turnRight(dir)
    yy, xx = y + dirR[0], x + dirR[1]
    if yy >= 0 and yy < m and xx >= 0 and xx < n:
        heapq.heappush(PQ, (heatLoss + grid[yy][xx], yy, xx, 1, dirIndex(dirR)) )
