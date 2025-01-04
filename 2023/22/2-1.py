# Very slow solution, takes more than an hour to run on the official input

from aoc import *
from copy import deepcopy

def onSegment(T, A, B):
    return ( (T.x <= max(A.x, B.x)) and (T.x >= min(A.x, B.x)) and 
           (T.y <= max(A.y, B.y)) and (T.y >= min(A.y, B.y)))

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

@timing
def dropDown(fromPos=0):
    global bricks
    nDropped = 0
    
    i = fromPos
    while i < len(bricks):
        if min(bricks[i][0].z, bricks[i][1].z) <= 1:
            i += 1
            continue
        
        minStep = 10 ** 10
        for j in range(i):
            if below(bricks[j], bricks[i]):
                dropStep = min(bricks[i][0].z, bricks[i][1].z) - max(bricks[j][0].z, bricks[j][1].z)
                if dropStep < minStep:
                    minStep = dropStep
        
        if minStep == 10 ** 10:
            minStep = min(bricks[i][0].z, bricks[i][1].z)
        if minStep > 1:
            bricks[i] = drop(bricks[i], minStep - 1)
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

dropDown()

bricksBackup = deepcopy(bricks)

n = len(bricks)
sumBricks = 0
for i in range(n-1):    
    print(i, end=': ')
    bricks = deepcopy(bricksBackup)
    bricks.pop(i)
    nBricks = dropDown(fromPos=i)
    sumBricks += nBricks

print(sumBricks)
