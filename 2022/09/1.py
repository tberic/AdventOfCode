fin = open('input.txt', 'r')

[x, y] = [0, 0]
[tailx, taily] = [0, 0]

visited = { (tailx, taily) }

for line in fin:
    [dir, steps] = line.split()
    steps = int(steps)
    
    for step in range(steps):
        if (dir == 'U'):
            x -= 1
        if (dir == 'D'):
            x += 1
        if (dir == 'L'):
            y -= 1
        if (dir == 'R'):
            y += 1
        
        if y == taily and x > tailx + 1:
            tailx += 1
        if y == taily and x < tailx - 1:
            tailx -= 1
        if x == tailx and y > taily + 1:
            taily += 1
        if x == tailx and y < taily - 1:
            taily -= 1

        if y == taily+1 and x > tailx + 1:
            tailx += 1
            taily += 1
        if y == taily+1 and x < tailx - 1:
            tailx -= 1
            taily += 1
        if y == taily-1 and x > tailx + 1:
            tailx += 1
            taily -= 1
        if y == taily-1 and x < tailx - 1:
            tailx -= 1
            taily -= 1
        if x == tailx+1 and y > taily + 1:
            taily += 1
            tailx += 1
        if x == tailx+1 and y < taily - 1:
            taily -= 1
            tailx += 1
        if x == tailx-1 and y > taily + 1:
            taily += 1
            tailx -= 1
        if x == tailx-1 and y < taily - 1:
            taily -= 1
            tailx -= 1
    
        visited.add((tailx, taily))

print(len(visited))