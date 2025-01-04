from aoc import *

TEST_AREA_X_MIN = 200000000000000
TEST_AREA_X_MAX = 400000000000000
TEST_AREA_Y_MIN = 200000000000000
TEST_AREA_Y_MAX = 400000000000000

def insideTestArea(T):
    return T.x >= TEST_AREA_X_MIN and T.x <= TEST_AREA_X_MAX and \
          T.y >= TEST_AREA_Y_MIN and T.y <= TEST_AREA_Y_MAX

def det(r, s):
    return r.x * s.y - r.y * s.x

def parallel(r, s):
    return det(r, s) == 0

def intersect(i, j):
    global pos, vel
    T1 = pos[i].project()
    r = vel[i].project()

    T2 = pos[j].project()
    s = vel[j].project()

    if parallel(r, s):
        # print('parallel')
        # print()
        return None
    
    x1 = T1.x
    x2 = T2.x
    y1 = T1.y
    y2 = T2.y
    a1 = r.x
    b1 = r.y
    a2 = s.x
    b2 = s.y
    D = -det(r, s)

    A = [[-b2 / D, a2 / D], [-b1 / D, a1 / D]]
    B = [[x2 - x1], [y2 - y1]]

    coeff = [[sum(a*b for a, b in zip(A_row, B_col)) for B_col in zip(*B)] for A_row in A]
    solX = x1 + coeff[0][0] * a1
    solY = y1 + coeff[0][0] * b1

    if coeff[0][0] < 0 or coeff[1][0] < 0:
        # print('Intersected in the past')
        # print()
        return None

    # print(A, B)
    # print(solX, solY)
    # print()

    return Point2(solX, solY)

f = open('input.txt', 'r')

pos = []
vel = []

for line in f:
    posString, velString = line.strip().split(' @ ')
    x, y, z = [int(i) for i in posString.split(',')]
    vx, vy, vz = [int(i) for i in velString.split(',')]

    pos.append(Point3(x, y, z))
    vel.append(Point3(vx, vy, vz))

count = 0
for i in range(len(pos)):
    for j in range(i+1, len(pos)):
        T = intersect(i, j)
        if T and insideTestArea(T):
            count += 1
print(count)