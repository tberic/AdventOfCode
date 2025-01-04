from aoc import *

print(vectorDist( (1, 2, 3), (1, 1, 1) ))
# print(vectorDist( (1, 2, 3), (1, 1, 1, 3) ))

mat = [[i*(j+2) for j in range(5)] for i in range(5)]
matrixPrint(mat)
print()
matrixPrint(matrixRot(mat))
print()
matrixPrint(matrixTranspose(mat))
print()