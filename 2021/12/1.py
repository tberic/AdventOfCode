from collections import defaultdict

paths = 0

def countPaths(x):
    global paths

    if x == 'end':
        paths += 1
        return
    
    if (visited[x]):
        return

    if x.isupper() == False:
        visited[x] = 1

    for i in graph[x]:
        countPaths(i)

    visited[x] = 0


f = open('input.txt', 'r')

graph = defaultdict(dict)
names = set()

for line in f:
    a, b = line.strip().split('-')
    graph[ a ][ b ] = 1
    graph[ b ][ a ] = 1
    names.add(a)
    names.add(b)

visited = { x: 0 for x in names }
    
countPaths('start')
print(paths)

f.close()