from aoc import *

def remove_edge(node1, node2):
    global V, E

    E[node1].remove(node2)
    E[node2].remove(node1)

@timing
def find_components():
    global V, E

    components = []
    
    VV = V.copy()
    while VV:
        Q = [VV[0]]
        visited = set()

        while Q:
            curNode = Q.pop(0)

            if curNode in visited:
                continue
            visited.add(curNode)
            VV.remove(curNode)

            for node in E[curNode]:
                Q.append(node)

        components.append(len(visited))

    return components

f = open('input.txt', 'r')

V = []
E = {}

for line in f:
    fromNode, toNodes = line.strip().split(': ')
    nodes = toNodes.split(' ')
    if fromNode not in V:
        V.append(fromNode)
    if fromNode not in E:
        E[fromNode] = []
    E[fromNode] += nodes
    for node in nodes:
        if node not in E:
            E[node] = []
        E[node] += [fromNode]
        if node not in V:
            V.append(node)

# edges = 0
# for edge in E.items():
#     nodes = ", ".join(edge[1])
#     print(edge[0] + ' -> ' + nodes)
#     # edges += len(edge[1])


# for node1 in V:
#     if node1 in E:
#         for node2 in E[node1]:
#             print(node1 + "-" + node2, end=", ")

# print(edges)

# print(V)
# print(E)

print(find_components())

remove_edge('zlv', 'bmx')
remove_edge('xsl', 'tpb')
remove_edge('lrd', 'qpg')

print(find_components())