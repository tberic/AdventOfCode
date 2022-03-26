import re

f = open('input.txt', 'r')
lines = [line.strip() for line in f]
f.close()

register = { "a": 1, "b": 0 }

i = 0
while (0 <= i < len(lines)):
    instruction, *l = re.split(' |, ', lines[i])   
    
    if instruction == "hlf":
        register[ l[0] ] //= 2
    elif instruction == "tpl":
        register[ l[0] ] *= 3
    elif instruction == "inc":
        register[ l[0] ] += 1
    elif instruction == "jmp":
        i += int(l[0])
        continue
    elif instruction == "jie":
        if register[ l[0] ] % 2 == 0:
            i += int(l[1])
            continue
    elif instruction == "jio":
        if register[ l[0] ] == 1:
            i += int(l[1])
            continue
    
    i += 1

print(register["b"])