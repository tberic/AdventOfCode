f = open('input.txt', 'r')
instruction = f.readline().strip().split(', ')
f.close()

dir = [(0, +1), (+1, 0), (0, -1), (-1, 0)]

x, y = (0, 0)

visited = [[0 for j in range(-200, 200)] for i in range(-200, 200)]

facing = 0
done = 0
for i in instruction:
    if i[0]=='R':
        facing = (facing+1)%4
    elif i[0]=='L':
        facing = (facing-1)%4
    
    for a in range(1, int(i[1:])+1):
        if visited[ x + a*dir[facing][0] + 200 ][ y + a*dir[facing][1] + 200 ]:
            print( x + a*dir[facing][0], y + a*dir[facing][1] )
            done = 1
            break
        visited[ x + a*dir[facing][0] + 200 ][ y + a*dir[facing][1] + 200 ] = 1

    if done:
        x = x + a*dir[facing][0]
        y = y + a*dir[facing][1]
        break

    x = x + int(i[1:])*dir[facing][0]
    y = y + int(i[1:])*dir[facing][1]

print( abs(x)+abs(y) )