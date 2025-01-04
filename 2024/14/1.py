def move(pos, vel):
    y = (pos[0] + vel[0] + M) % M
    x = (pos[1] + vel[1] + N) % N

    return (y, x)

f = open('input.txt')

STEPS = 100
M = 103
N = 101
# M = 7
# N = 11

# grid = [["" for j in range(N)] for i in range(M)]

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
    # grid[y][x] += str(id)+":"+str(velx)+":"+str(vely)+" "

for step in range(STEPS):
    for id in range(len(positions)):
        positions[id] = move(positions[id], velocities[id])

quad1 = 0
quad2 = 0
quad3 = 0
quad4 = 0
print(positions)
for id in range(len(positions)):
    if positions[id][0] < M // 2 and positions[id][1] < N // 2:
        quad1 += 1
    elif positions[id][0] < M // 2 and positions[id][1] > N // 2:
        quad2 += 1
    elif positions[id][0] > M // 2 and positions[id][1] < N // 2:
        quad3 += 1
    elif positions[id][0] > M // 2 and positions[id][1] > N // 2:
        quad4 += 1

print(quad1 * quad2 * quad3 * quad4)