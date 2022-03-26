from collections import deque

def draw(c):
    if c:
        return '#'
    else:
        return '.'

def wall(x, y):
    global magic
    n = x*x + 3*x + 2*x*y + y + y*y + magic
    return sum(map(int, bin(n)[2:])) % 2

f = open('input.txt', 'r')
magic = int(f.readline().strip())
f.close()

# we'll look for the shortest path using BFS

Q = deque([(1, 1, 0)])
visited = {}
visited[(1, 1)] = 0

while True:
    x, y, d = Q.popleft()
    visited[ (x,y) ] = d

    if (x, y) == (31, 39):
        print(d)
        break

    if x > 0 and not wall(x-1, y) and (x-1, y) not in visited:
        Q.append( (x-1, y, d+1) )
        #visited[ (x-1,y) ] = d+1
    if not wall(x+1, y) and (x+1, y) not in visited:
        Q.append( (x+1, y, d+1) )
        #visited[ (x+1,y) ] = d+1
    if y > 0 and not wall(x, y-1) and (x, y-1) not in visited:
        Q.append( (x, y-1, d+1) )
        #visited[ (x,y-1) ] = d+1
    if not wall(x, y+1) and (x, y+1) not in visited:
        Q.append( (x, y+1, d+1) )
        #visited[ (x,y+1) ] = d+1

count = 0
for (x, y) in visited:
    if visited[(x,y)] <= 50:
        count += 1
print(count)


#magic = 10

# for x in range(40):
#     for y in range(40):
#         print(f'{draw(wall(y,x)):>1}', end='')
#     print()

# for x in range(40):
#     for y in range(40):
#         if (y,x) in visited:
#             print(f'{visited[(y,x)]:>3}', end='')
#         else:
#             c = '#'
#             print(f'{c:>3}', end='')
#     print()
