import numpy as np

def move(pos, vel):
    y = (pos[0] + vel[0] + M) % M
    x = (pos[1] + vel[1] + N) % N

    return (y, x)

f = open('input.txt')

STEPS = 100000
M = 103
N = 101
# M = 7
# N = 11

positions = []
velocities = []
for line in f:
    pos, vel = line.strip().split(' ')
    _, pos = pos.split('=')
    _, vel = vel.split('=')
    
    x, y = list(map(int, pos.split(',')))
    velx, vely = list(map(int, vel.split(',')))
    positions.append((y, x))
    velocities.append((vely, velx))

grid = [ ['.' for x in range(M)] for y in range(M) ]

step = 0
minVar = 10**10
while True:
    step += 1

    grid = [ ['.' for x in range(M)] for y in range(M) ]
    for id in range(len(positions)):
        positions[id] = move(positions[id], velocities[id])
        grid[positions[id][0]][positions[id][1]] = '*'

    yCoords = [ position[0] for position in positions ]
    xCoords = [ position[1] for position in positions ]
    varianceY = np.var(yCoords)
    varianceX = np.var(xCoords)
    if varianceY * varianceX < minVar:
        minVar = varianceY * varianceX
        for y in range(M):
            for x in range(N):
                print(grid[y][x], end='')
            print()
        print(step, minVar)
        input()

    if step % 1000 == 0:
        print(step)