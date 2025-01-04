import time
import random
from copy import deepcopy

def change(starts_with, new_val):
    for i in range(45):
        change_bit(starts_with, i, 0)

    bin_val = bin(new_val)[2:]
    bin_val = bin_val.zfill(45)
    for i in range(len(bin_val)):
        change_bit(starts_with, 44-i, int(bin_val[i]))

def change_bit(starts_with, order, new_val):
    for wire in wires.keys():
        if wire[0] == starts_with and int(wire[1:]) == order:
            wires[wire] = new_val

def parse_wires(start_with):
    sol = 0
    for wire, val in wires.items():
        if wire[0] == start_with:
            order = int(wire[1:])
            if val:
                sol |= 2 ** order
    return sol

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

for i, (gate, val) in enumerate(gates.items()):
    print(val[0] + "->" + val[1] + str(i))
    print(val[2] + "->" + val[1] + str(i))
    print(val[1] + str(i) + "->" + gate)