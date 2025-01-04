from collections import OrderedDict

def HASH(s):
    hash = 0
    for c in s:
        hash += ord(c)
        hash *= 17
        hash %= 256

    return hash

f = open('input.txt', 'r')

lines = [line.strip() for line in f]
line = lines[0]
cmds = line.split(',')

boxes = [OrderedDict() for i in range(256)]
for cmd in cmds:
    if cmd[-1] in "123456789":
        label = cmd[:-2]
        op = cmd[-2]
        focal = int(cmd[-1])                    
    else:
        label = cmd[:-1]
        op = cmd[-1]

    hash = HASH(label)    

    if op == '=':
        boxes[hash][label] = focal
    elif op == '-':
        if label in boxes[hash]:
            boxes[hash].pop(label)
    else:
        print('Error')

power = 0
for i, box in enumerate(boxes):
    pos = 0
    for key, value in box.items():
        pos += 1
        power += (i+1) * pos * value

print(power)