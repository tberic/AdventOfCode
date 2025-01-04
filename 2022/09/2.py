def update_position(x, y, tailx, taily):
    if y == taily and x > tailx + 1:
        tailx += 1
    if y == taily and x < tailx - 1:
        tailx -= 1
    if x == tailx and y > taily + 1:
        taily += 1
    if x == tailx and y < taily - 1:
        taily -= 1

    if y > taily and x > tailx + 1:
        tailx += 1
        taily += 1
    if y > taily and x < tailx - 1:
        tailx -= 1
        taily += 1
    if y < taily and x > tailx + 1:
        tailx += 1
        taily -= 1
    if y < taily and x < tailx - 1:
        tailx -= 1
        taily -= 1
    if x > tailx and y > taily + 1:
        taily += 1
        tailx += 1
    if x > tailx and y < taily - 1:
        taily -= 1
        tailx += 1
    if x < tailx and y > taily + 1:
        taily += 1
        tailx -= 1
    if x < tailx and y < taily - 1:
        taily -= 1
        tailx -= 1
    
    return (tailx, taily)


fin = open('input.txt', 'r')

x = [0 for i in range(10)]
y = [0 for i in range(10)]

visited = { (0, 0) }

for line in fin:
    [dir, steps] = line.split()
    steps = int(steps)
    
    for step in range(steps):
        if (dir == 'U'):
            x[0] -= 1
        if (dir == 'D'):
            x[0] += 1
        if (dir == 'L'):
            y[0] -= 1
        if (dir == 'R'):
            y[0] += 1
        
        for i in range(1, 10):
            (x[i], y[i]) = update_position(x[i-1], y[i-1], x[i], y[i])
        visited.add((x[9], y[9]))

    #print(x)
    #print(y)

print(len(visited))