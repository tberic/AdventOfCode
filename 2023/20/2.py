from aoc import *

LOW = 0
HIGH = 1

modules = {}
types = {}
state = {}

def send_pulse(start_node, target_node):
    global pulsesLow, pulsesHigh, turnedOn

    Q = [('broadcaster', start_node, LOW)]
    
    pulse_on_target = False
    while Q:
        origin, node, pulse = Q.pop(0)

        if node == target_node and pulse == LOW:
            pulse_on_target = True
        elif types[node] == '%':
            if pulse == HIGH:
                pass
            else:
                if state[node] == 0:
                    state[node] = 1
                    pulse = HIGH
                else:
                    state[node] = 0
                    pulse = LOW
                
                for out in modules[node]:
                    Q.append( (node, out, pulse) )

        elif types[node] == '&':
            state[node][origin] = pulse
            
            if all( [state[node][origin] == HIGH for origin in state[node] ] ):
                pulse = LOW
            else:
                pulse = HIGH

            for out in modules[node]:
                Q.append( (node, out, pulse) )

    return pulse_on_target


f = open('input.txt', 'r')
lines = [line.strip() for line in f]

for line in lines:
    input, outputs = line.split(' -> ')

    if input[0] in "%&":
        inputType = input[0]
        inputName = input[1:]
    else:
        inputType = ' '
        inputName = input

    if inputType == ' ':
        state[inputName] = 0
    elif inputType == '%':
        state[inputName] = 0
    elif inputType == '&':
        state[inputName] = {}

    modules[inputName] = []
    types[inputName] = inputType
    for output in outputs.split(', '):
        modules[inputName].append(output)

# find nodes that didn't appear as inputs and add them
nodes = []
for node in modules:
    for out in modules[node]:
        if out not in modules:
            nodes.append(out)

for node in nodes:
    modules[node] = []
    types[node] = ' '
    state[node] = 0

# update & node states by keeping track of their inputs
for node in modules:
    for out in modules[node]:
        if types[out] == '&':
            state[out][node] = LOW

# print(modules)
# print(types)
# print(state)

i1 = 0
while True:
    pulse = send_pulse('ss', 'ph')
    i1 += 1    
    if pulse:
        break
print(i1)

i2 = 0
while True:
    pulse = send_pulse('vq', 'tx')
    i2 += 1    
    if pulse:
        break
print(i2)

i3 = 0
while True:
    pulse = send_pulse('qg', 'nz')
    i3 += 1
    if pulse:
        break
print(i3)

i4 = 0
while True:
    pulse = send_pulse('kb', 'dd')
    i4 += 1
    if pulse:
        break
print(i4)

print(i1 * i2 * i3 * i4)