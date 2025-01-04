from aoc import *
from functools import lru_cache

def isConnected(fromNode, toNode):
    global V, E
    if fromNode not in V or toNode not in V:
        return False
    if fromNode not in E:
        return False
    for edge in E[fromNode]:
        node, weight = edge
        if node == toNode:
            return True
    return False

def isIntersection(y, x):
    global grid
    up = y > 0 and grid[y - 1][x] in '<>^v'
    down = y < len(grid) - 1 and grid[y + 1][x] in '<>^v'
    left = x > 0 and grid[y][x - 1] in '<>^v'
    right = x < len(grid[0]) - 1 and grid[y][x + 1] in '<>^v'
    return up + down + left + right > 2

# @lru_cache(maxsize=None)
def walk(node, steps):
    global V, E, endPoint, maxSteps, visitedNodes

    if node == endPoint:
        if steps > maxSteps:
            # print(path)
            maxSteps = steps        
        return

    if node in visitedNodes:
        return
    
    visitedNodes.add(node)
   
    for edge in E[node]:
        walk( edge[0], steps + edge[1] )

    visitedNodes.remove(node)


f = open('input.txt', 'r')

grid = [line.strip() for line in f]

startPoint = (0, 1)
endPoint = (len(grid) - 1, len(grid[0]) - 2)

V = [ startPoint ]
E = { startPoint: [] }

visited = [[0 for j in range(len(grid[0]))] for i in range(len(grid))]

visited[startPoint[0]][startPoint[1]] = 1
startPointDown = (startPoint[0] + DOWN[0], startPoint[1] + DOWN[1])
Q = [(startPointDown, 1, startPoint)]

while Q:
    (y, x), steps, fromNode = Q.pop(0)
    # print(y, x, steps)

    if visited[y][x]:
        continue

    if (y, x) in V and isConnected(fromNode, (y, x)):
        continue

    visited[y][x] = 1

    if (y, x) == endPoint:
        V.append(endPoint)
        E[fromNode].append( ( endPoint, steps ) )
        continue

    up = down = left = right = False
    if grid[y][x] == '^':
        up = True
    elif grid[y][x] == 'v':
        down = True
    elif grid[y][x] == '<':
        left = True
    elif grid[y][x] == '>':
        right = True
    elif grid[y][x] == '.':
        up = y > 0 and grid[y-1][x] in '^.' and not visited[y-1][x]
        down = y < len(grid)-1 and grid[y+1][x] in 'v.' and not visited[y+1][x]
        left = x > 0 and grid[y][x-1] in '<.' and not visited[y][x-1]
        right = x < len(grid[0])-1 and grid[y][x+1] in '>.' and not visited[y][x+1]

    directions = up + down + left + right
    # print(directions)

    if directions > 1 or (y, x) in V or isIntersection(y, x):
        if (y, x) not in V:
            V.append( (y, x) )
        if (y, x) not in E:
            E[(y, x)] = []
        
        E[fromNode].append( ((y,x), steps) )
        if fromNode != startPoint:
            E[(y, x)].append( (fromNode, steps) )

        steps = 0
        fromNode = (y, x)
        visited[y][x] = 0
            
    elif directions == 1:
        pass
    else:
        pass

    if up:
        Q.append( ((y-1, x), steps+1, fromNode) )
    if down:
        Q.append( ((y+1, x), steps+1, fromNode) )
    if left:
        Q.append( ((y, x-1), steps+1, fromNode) )
    if right:
        Q.append( ((y, x+1), steps+1, fromNode) )

# print(V)
# print(E)

for node in E:
    print(node, end=': ')
    for edge in E[node]:
        print( edge, end=' ' )
    print()

visitedNodes = set()

maxSteps = 0
walk(V[0], 0)
print(maxSteps)