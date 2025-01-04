from collections import defaultdict

max_clique = []

def BronKerbosch(R, P, X):
    if not P and not X:
        max_clique.append(R)
    for node in list(P):
        BronKerbosch(R | set([node]), P & set(connected[node]), X & set(connected[node]))
        P -= set([node])
        X |= set([node])


f = open('input.txt')

nodes = set()
connected = defaultdict(list)
for line in f:
    a, b = line.strip().split('-')
    nodes.add(a)
    nodes.add(b)
    connected[a].append(b)
    connected[b].append(a)

BronKerbosch(set(), set(nodes), set())

max_clique = sorted(max_clique, key = lambda x: len(x), reverse=True)
print(",".join(sorted(max_clique[0])))