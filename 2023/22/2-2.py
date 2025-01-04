# TODO: have to update the height grid better
# doesn't count dropped bricks correctly

from aoc import *
from copy import deepcopy

def isXAligned(A, B):
    return A.y == B.y

def isYAligned(A, B):
    return A.x == B.x

def intersects(A1, A2, B1, B2):
    x1 = min(A1.x, A2.x)
    x2 = max(A1.x, A2.x)
    x3 = min(B1.x, B2.x)
    x4 = max(B1.x, B2.x)
    y1 = min(A1.y, A2.y)
    y2 = max(A1.y, A2.y)
    y3 = min(B1.y, B2.y)
    y4 = max(B1.y, B2.y)

    if isXAligned(A1, A2) and isXAligned(B1, B2):
        if A1.y != B1.y:
            return False
        return (x1 <= x3 and x3 <= x2) or (x1 <= x4 and x4 <= x2) or \
               (x3 <= x1 and x1 <= x4) or (x3 <= x2 and x2 <= x4)
    if isYAligned(A1, A2) and isYAligned(B1, B2):
        if A1.x != B1.x:
            return False
        return (y1 <= y3 and y3 <= y2) or (y1 <= y4 and y4 <= y2) or \
               (y3 <= y1 and y1 <= y4) or (y3 <= y2 and y2 <= y4)
    if isXAligned(A1, A2) and isYAligned(B1, B2):
        if B1.x < x1 or B1.x > x2:
            return False
        return y3 <= y1 and y1 <= y4
    if isYAligned(A1, A2) and isXAligned(B1, B2):
        return intersects(B1, B2, A1, A2)


def below(brick1, brick2):
    return intersects( brick1[0].project(), brick1[1].project(), \
                       brick2[0].project(), brick2[1].project() ) \
            and max(brick1[0].z, brick1[1].z) < min(brick2[0].z, brick2[1].z)

def drop(brick, step=1):
    A = brick[0]
    B = brick[1]
    A.z -= step
    B.z -= step
    return (A, B)

def update_height(brick):
    global height

    x1 = min(brick[0].x, brick[1].x)
    x2 = max(brick[0].x, brick[1].x)
    y1 = min(brick[0].y, brick[1].y)
    y2 = max(brick[0].y, brick[1].y)
    z = max(brick[0].z, brick[1].z)

    if isXAligned(brick[0], brick[1]):
        for y in range(y1, y2+1):
            if z > height[x1][y]:
                height[x1][y] = z
    if isYAligned(brick[0], brick[1]):
        for x in range(x1, x2+1):
            if z > height[x][y1]:
                height[x][y1] = z

def update_heights(toPos):
    global bricks
    for i in range(toPos+1):
        update_height(bricks[i])

@timing
def dropDown(fromPos=0):
    global bricks, height
    nDropped = 0
    
    i = fromPos
    while i < len(bricks):
        if min(bricks[i][0].z, bricks[i][1].z) <= 1:
            i += 1
            continue
        
        maxHeight = 0
        x1 = min(bricks[i][0].x, bricks[i][1].x)
        x2 = max(bricks[i][0].x, bricks[i][1].x)
        y1 = min(bricks[i][0].y, bricks[i][1].y)
        y2 = max(bricks[i][0].y, bricks[i][1].y)
        if x1 == x2:
            for y in range(y1, y2 + 1):
                if height[x1][y] > maxHeight:
                    maxHeight = height[x1][y]
        elif y1 == y2:
            for x in range(x1, x2 + 1):
                if height[x][y1] > maxHeight:
                    maxHeight = height[x][y1]

        step = min(bricks[i][0].z, bricks[i][1].z) - maxHeight
        if step > 1:
            bricks[i] = drop(bricks[i], step-1)
            update_height(bricks[i])
            nDropped += 1

        i += 1

    return nDropped

MAXN = 350

f = open('input.txt', 'r')

bricks = []

for line in f:
    A, B = line.strip().split('~')
    x1, y1, z1 = [int(coord) for coord in A.split(',')]
    x2, y2, z2 = [int(coord) for coord in B.split(',')]

    bricks.append( (Point3(x1, y1, z1), Point3(x2, y2, z2)) )

bricks = sorted(bricks, key = lambda brick: min(brick[0].z, brick[1].z) )

height = [[0 for j in range(MAXN)] for i in range(MAXN)]
zeroHeight = deepcopy(height)

n = dropDown()
print(n)

bricksBackup = deepcopy(bricks)

n = len(bricks)
countBricks = 0
for i in range(n-1):
    # print(i, end=': ')
    bricks = deepcopy(bricksBackup)
    bricks.pop(i)
    height = deepcopy(zeroHeight)
    update_heights(toPos=i)
    nBricks = dropDown(fromPos=i)
    countBricks += nBricks

print(countBricks)
