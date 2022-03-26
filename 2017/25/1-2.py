from collections import deque

def getValue(pos):
    global tape
    if pos < 0:
        tape.appendleft(0)
        return 0, 0
    elif pos == len(tape):
        tape.append(0)
        return 0, len(tape)-1
    else:
        return tape[pos], pos
        

steps = 12667664
state = 0
cursor = 0
tape = deque([0])

for _ in range(steps):
    x, cursor = getValue(cursor)
    
    if state == 0: #state A
        if x == 0:
            tape[cursor] = 1
            cursor += 1
            state = 1
        elif x == 1:
            tape[cursor] = 0
            cursor -= 1
            state = 2
    elif state == 1: #state B
        if x == 0:
            tape[cursor] = 1
            cursor -= 1
            state = 0
        elif x == 1:
            tape[cursor] = 1
            cursor += 1
            state = 3
    elif state == 2: #state C
        if x == 0:
            tape[cursor] = 0
            cursor -= 1
            state = 1
        elif x == 1:
            tape[cursor] = 0
            cursor -= 1
            state = 4
    elif state == 3: #state D
        if x == 0:
            tape[cursor] = 1
            cursor += 1
            state = 0
        elif x == 1:
            tape[cursor] = 0
            cursor += 1
            state = 1
    elif state == 4: #state E
        if x == 0:
            tape[cursor] = 1
            cursor -= 1
            state = 5
        elif x == 1:
            tape[cursor] = 1
            cursor -= 1
            state = 2
    elif state == 5: #state F
        if x == 0:
            tape[cursor] = 1
            cursor += 1
            state = 3
        elif x == 1:
            tape[cursor] = 1
            cursor += 1
            state = 0

    #print(x, cursor, tape)

print(sum(tape))