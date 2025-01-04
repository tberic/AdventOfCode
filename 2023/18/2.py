from aoc import *

f = open('input.txt', 'r')

lines = [line.strip() for line in f]

dirs = {'0': RIGHT, '2': LEFT, '1': DOWN, '3': UP}

vertices = [(0, 0)]

y, x = 0, 0
border = 0
for line in lines:    
    _, _, instruction = line.split(' ')
    instruction = instruction[2:-1]

    n = int(instruction[:-1], 16)
    dir = dirs[instruction[-1]]
    
    border += n
    y += n * dir[0]
    x += n * dir[1]
    vertices.append((y,x))


# Shoelace formula
A = polygonArea(vertices[:-1])
# Pick's theorem
print(A + border/2 + 1)