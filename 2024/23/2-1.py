def flood_fill(*args):
    latest_node = args[-1]
    if visited[latest_node]:
        return
    visited[latest_node] = 1

    for j in range(len(nodes)):
        pass

# def find_max(size, *args):
#     latest_node = args[-1]
#     max_size = 0
#     best_subgraph = []
#     print(latest_node)
#     for node in connected[latest_node]:
#         good = True
#         for existing_node in args:
#             if not graph[ pos[node] ][ pos[existing_node] ]:
#                 good = False
#         if good:
#             new_size, subgraph = find_max(size+1, *args, node)
#             if new_size > max_size:
#                 max_size = new_size
#                 best_subgraph = subgraph
#     return max_size, best_subgraph

f = open('input0.txt')

nodes = []
pos = {}
graph = [[0 for j in range(1000)] for i in range(1000)]
connected = {}
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
    if a not in connected:        
        connected[a] = [b]
    else:
        connected[a].append(b)
    if b not in connected:
        connected[b] = [a]
    else:
        connected[b].append(a)

# degree = [0 for i in range(len(nodes))]
# for i in range(len(nodes)):
#     degree[i] = len(connected[nodes[i]])
#     print(nodes[i], degree[i])
    
# print(max(degree))

max_size = 0
for i, node in enumerate(nodes):
    visited = [0 for i in range(len(nodes))]
    flood_fill(i)
    size = sum(visited)
    if size > max_size:
        pass

print(max_size)