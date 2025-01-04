import time

def simulate(wires, gates):
    while gates:
        keys_to_remove = []
        for output, gate in gates.items():
            if gate[0] in wires and gate[2] in wires:
                if gate[1] == 'OR':
                    val = wires[gate[0]] | wires[gate[2]]
                elif gate[1] == 'AND':
                    val = wires[gate[0]] & wires[gate[2]]
                elif gate[1] == 'XOR':
                    val = wires[gate[0]] ^ wires[gate[2]]
                else:
                    print('Error, unexpected operand')

                wires[output] = val
                keys_to_remove.append(output)
                
        for key in keys_to_remove:
            del gates[key]


f = open('input.txt')

wires = {}
gates = {}
wiresInput = True
for line in f:
    if line == '\n':
        wiresInput = False
        continue

    if wiresInput:
        name, val = line.strip().split(': ')
        val = int(val)
        wires[name] = val
    else:
        left, c = line.strip().split(' -> ')
        a, op, b = left.split(' ')

        gates[c] = (a, op, b)

# print(len(wires))
# print(len(gates))

start = time.time()
simulate(wires, gates)
end = time.time()
print(wires)
print(gates)

sol = 0
for wire, val in wires.items():
    if wire[0] == 'z':
        order = int(wire[1:])
        if val:
            sol |= 2 ** order

print(sol)
print(f"{end - start} ms")