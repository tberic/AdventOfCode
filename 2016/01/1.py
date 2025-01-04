f = open('input.txt', 'r')
instruction = f.readline().strip().split(', ')
f.close()

dir = [(0, +1), (+1, 0), (0, -1), (-1, 0)]

x, y = (0, 0)
facing = 0
for i in instruction:
    if i[0]=='R':
        facing = (facing+1)%4
    elif i[0]=='L':
        facing = (facing-1)%4
    
    x = x + int(i[1:])*dir[facing][0]
    y = y + int(i[1:])*dir[facing][1]
    #print(x, y)

print( abs(x)+abs(y) )