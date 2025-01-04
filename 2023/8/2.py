f = open('input.txt', 'r')

lines = [line.strip() for line in f if line.strip() != ""]

instructions = lines[0]
# print(instructions)

nodes = {}

for line in lines[1:]:
    node, dirs = line.split(' = ')
    left, right = dirs[1:-1].split(', ')
    nodes[node] = (left, right)

# print(nodes)

for startNode in nodes.keys():
    if startNode[2] == 'A':
        steps = 0
        node = startNode

        while node[2] != 'Z':
            for step in instructions:

                if node[2] == 'Z':
                    break

                if step == 'L':
                    node = nodes[node][0]
                elif step == 'R':
                    node = nodes[node][1]
                else:
                    print('Error')

                steps += 1

        print(steps)

# in the end take the lowest common denominator of all the outputted steps