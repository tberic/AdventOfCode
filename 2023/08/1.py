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

steps = 0
node = 'AAA'

while node != 'ZZZ':
    for step in instructions:

        if node == 'ZZZ':
            break

        if step == 'L':
            node = nodes[node][0]
        elif step == 'R':
            node = nodes[node][1]
        else:
            print('Error')

        steps += 1

print(steps)