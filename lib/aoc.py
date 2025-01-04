from functools import wraps
from time import time

def timing(f):
    @wraps(f)
    def wrap(*args, **kw):
        ts = time()
        result = f(*args, **kw)
        te = time()
        print('func: %r args: [%r, %r] took: %2.4f sec' % \
          (f.__name__, args, kw, te-ts))
        return result
    return wrap


UP = (-1, 0)
DOWN = (+1, 0)
LEFT = (0, -1)
RIGHT = (0, +1)

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


def vectorDist(A, B):
    if len(A) != len(B):
        raise TypeError("[AOC] dist: Vectors are not of the same length")
    return sum( abs(A[i] - B[i]) for i in range(len(A)) )

def matrixRot(A):
    m = len(A)
    n = len(A[0])
    if m != n:
        raise TypeError("[AOC] matrixRot: Matrix is not square")

    B = [[0 for j in range(n)] for i in range(m)]
    
    for i in range(n):
        for j in range(m):
            B[i][j] = A[m-j-1][i]
    
    return B

def matrixTranspose(A):
    B = [['.' for j in range(len(A))] for i in range(len(A[0]))]
    for i in range(len(A)):
        for j in range(len(A[0])):
            B[j][i] = A[i][j]
    return B

def matrixPrint(A, sep=' '):
    for i in range(len(A)):
        for j in range(len(A[0])):
            print(A[i][j], end=sep)
        print()

def vectorPrint(A, sep=' '):
    for x in A:
        print(x, end=sep)

def polygonArea(vertices):    
    n = len(vertices)
    sum1 = 0
    sum2 = 0

    for i in range(0, n-1):
        sum1 = sum1 + vertices[i][0] * vertices[i+1][1]
        sum2 = sum2 + vertices[i][1] * vertices[i+1][0]

    sum1 = sum1 + vertices[-1][0] * vertices[0][1]
    sum2 = sum2 + vertices[0][0] * vertices[-1][1]

    area = abs(sum1 - sum2) / 2
    return area
