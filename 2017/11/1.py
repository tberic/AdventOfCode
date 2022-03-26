def distance(a, b):
    dx = abs(a[1] - b[1])
    dy = abs(a[0] - b[0])
    return dy + max(0, (dx-dy)//2)

f = open('input.txt', 'r')
line = f.readline().strip()
f.close()

maxDist = 0
(x, y) = (0, 0)
for dir in line.split(','):
    if dir == "n":
        y -= 2
    elif dir == "s":
        y += 2
    elif dir == "ne":
        x += 1
        y -= 1
    elif dir == "nw":
        x -= 1
        y -= 1
    elif dir == "se":
        x += 1
        y += 1
    elif dir == "sw":
        x -= 1
        y += 1

    if distance( (x,y), (0, 0) ) > maxDist:
        maxDist = distance( (x,y), (0, 0) )

print(x, y)                   
print(distance( (x,y), (0, 0) ))
print(maxDist)