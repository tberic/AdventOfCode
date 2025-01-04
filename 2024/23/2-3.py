tried = {}

def find_max(size, *args):
    latest_node = args[-1]
    max_size = size
    graph_so_far = ",".join(sorted(args))
    best_subgraph = graph_so_far

    if best_subgraph in tried:
        return 0, None

    # print(max_size, best_subgraph)
    
    for node in connected[latest_node]:
        connected_to_all = True
        for existing_node in args:
            if not graph[ pos[node] ][ pos[existing_node] ]:
                connected_to_all = False
        if connected_to_all:
            new_size, subgraph = find_max(size+1, *args, node)
            if new_size > max_size:
                max_size = new_size
                best_subgraph = subgraph
    
    tried[graph_so_far] = 1

    return max_size, best_subgraph


f = open('input.txt')

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

max_size = 0
for node in nodes:
    print(node)
    size, subgraph = find_max(1, node)
    if size > max_size:
        max_size = size
        max_subgraph = subgraph

print(max_size, max_subgraph)