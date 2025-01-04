from aoc import *

class Point2:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return "(" + str(self.x) + "," + str(self.y) + ")"

class Point3:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __repr__(self):
        return "(" + str(self.x) + "," + str(self.y) + "," + str(self.z) + ")"
    
    def project(self):
        return Point2(self.x, self.y)

def onSegment(T, A, B):
    if ( (A.x <= max(T.x, B.x)) and (A.x >= min(T.x, B.x)) and 
           (A.y <= max(T.y, B.y)) and (A.y >= min(T.y, B.y))): 
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

def immediatelyBelow(brick1, brick2):
    z = min(brick2[0].z, brick2[1].z)
    if max(brick1[0].z, brick1[1].z) != z - 1:
        return False
    return intersects( brick1[0].project(), brick1[1].project(), \
                       brick2[0].project(), brick2[1].project() )

def drop(brick):
    A = brick[0]
    B = brick[1]
    A.z -= 1
    B.z -= 1
    brickNew = (A, B)
    return brickNew        

def dropDown(justOnce = False):
    global bricks
    nDropped = 0
    dropped = True
    while dropped:
        dropped = False
        i = 0
        while i < len(bricks):
            canDrop = True
            if min(bricks[i][0].z, bricks[i][1].z) <= 1:
                i += 1
                continue
            for brick in bricks:
                if brick != bricks[i] and immediatelyBelow(brick, bricks[i]):
                    canDrop = False
                    break

            if canDrop:
                if justOnce:
                    return True
                nDropped += 1
                bricks[i] = drop(bricks[i])
                dropped = True
            i += 1
    if justOnce:
        return False
    return nDropped > 0

MAXN = 350

f = open('input.txt', 'r')

bricks = []

# grid = [[[0 for k in range(MAXN)] for j in range(MAXN)] for i in range(MAXN)]

for line in f:
    A, B = line.strip().split('~')
    x1, y1, z1 = [int(coord) for coord in A.split(',')]
    x2, y2, z2 = [int(coord) for coord in B.split(',')]

    bricks.append( (Point3(x1, y1, z1), Point3(x2, y2, z2)) )

# print(bricks)

dropDown()

print('DROPPED')

n = len(bricks)
nSafe = 0
for i in range(n):
    print(i)
    brick = bricks.pop(0)
    res = dropDown(justOnce=True)
    if not res:
        nSafe += 1
    bricks.append(brick)

print(nSafe)

