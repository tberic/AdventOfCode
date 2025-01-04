from aoc import *

LOW = 0
HIGH = 1

pulsesHigh = 0
pulsesLow = 0

modules = {}
types = {}
state = {}

def send_pulse():
    global pulsesLow, pulsesHigh

    Q = [('button', 'broadcaster', LOW)]
    
    while Q:
        origin, node, pulse = Q.pop(0)
        # print(origin, node, pulse)

        if pulse == HIGH:
            pulsesHigh += 1
        else:
            pulsesLow += 1

        if types[node] == ' ' and node == 'broadcaster':
            for out in modules[node]:
                Q.append( (node, out, pulse) )

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


        # for out in modules[node]:
        #     Q.append( (out, pulse) )





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

print(modules)
print(types)
print(state)
        
# send_pulse()

for i in range(1000):
    send_pulse()

print(pulsesLow * pulsesHigh)