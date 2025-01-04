f = open('input.txt')

nodes = []
pos = {}
graph = [[0 for j in range(1000)] for i in range(1000)]

for line in f:
    a, b = line.strip().split('-')
    if a not in nodes:
        nodes.append(a)
        pos[a] = len(nodes) - 1
    if b not in nodes:
        nodes.append(b)
        pos[b] = len(nodes) - 1
    
    graph[ pos[a] ][ pos[b] ] = 1
    graph[ pos[b] ][ pos[a] ] = 1

total = 0
for i in range(len(nodes)):
    for j in range(i+1, len(nodes)):
        for k in range(j+1, len(nodes)):
            if graph[i][j] and graph[j][k] and graph[k][i]:
                if nodes[i][0] == 't' or nodes[j][0] == 't' or nodes[k][0] == 't':
                    total += 1

print(total)