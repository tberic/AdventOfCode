from aoc import *

def onSegment(T, A, B):
    if ( (T.x <= max(A.x, B.x)) and (T.x >= min(A.x, B.x)) and 
           (T.y <= max(A.y, B.y)) and (T.y >= min(A.y, B.y))): 
        return True
    return False

# ccw or counter ccw (or colinear points)
def orientation(A, B, C):
    area2 = ((B.y - A.y) * (C.x - B.x)) - ((B.x - A.x) * (C.y - B.y))
    if area2 > 0:
        return 1
    if area2 < 0:
        return -1
    return 0

def intersects(A1, A2, B1, B2):
    if A1 == A2 and onSegment(A1, B1, B2):
        return True
    if B1 == B2 and onSegment(B1, A1, A2):
        return True

    o1 = orientation(A1, A2, B1) 
    o2 = orientation(A1, A2, B2)
    o3 = orientation(B1, B2, A1)
    o4 = orientation(B1, B2, A2)
  
    if ((o1 != o2) and (o3 != o4)): 
        return True
  
    if ((o1 == 0) and onSegment(A1, B1, A2)):
        return True
  
    # p1 , q1 and q2 are collinear and q2 lies on segment p1q1 
    if ((o2 == 0) and onSegment(A1, B2, A2)): 
        return True
  
    # p2 , q2 and p1 are collinear and p1 lies on segment p2q2 
    if ((o3 == 0) and onSegment(B1, A1, B2)): 
        return True
  
    # p2 , q2 and q1 are collinear and q1 lies on segment p2q2 
    if ((o4 == 0) and onSegment(B1, A2, B2)): 
        return True
  
    # If none of the cases 
    return False

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

# print(bricks)

dropDown()

print('DROPPED')
# print(bricks)

# n = len(bricks)
# sumBricks = 0
# for i in range(n-1):
#     print(i)
#     bricksBackup = bricks.copy()
#     brick = bricks.pop(i)
#     nBricks = dropDown(fromPos=i)
#     print(nBricks)
#     sumBricks += nBricks
#     # bricks.insert(i, brick)
#     bricks = bricksBackup.copy()

# # print(bricks)

# print(sumBricks)
