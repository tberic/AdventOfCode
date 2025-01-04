from copy import deepcopy

def combo(x, reg):
    if x >= 0 and x <= 3:
        return x
    if x >= 4 and x <= 6:
        return reg[x-4]
    print('Error')

def run(prog, reg):
    index = 0
    output = []
    while index < len(prog):
        op = prog[index]
        operand = prog[index+1]

        if op == 0:
            reg[0] = reg[0] // (2 ** combo(operand, reg))
        elif op == 1:
            reg[1] = reg[1] ^ operand
        elif op == 2:
            reg[1] = combo(operand, reg) % 8
        elif op == 3:
            if reg[0] != 0:
                index = operand
                continue
        elif op == 4:
            reg[1] = reg[1] ^ reg[2]
        elif op == 5:
            output.append(combo(operand, reg) % 8)
        elif op == 6:
            reg[1] = reg[0] // (2 ** combo(operand, reg))
        elif op == 7:
            reg[2] = reg[0] // (2 ** combo(operand, reg))

        index += 2
    
    return output


f = open('input.txt')

lines = [line.strip() for line in f]
reg = [0, 0, 0]
for i in range(3):
    _, regTxt = lines[i].split(': ')
    reg[i] = int(regTxt)

_, progTxt = lines[4].split(': ')
prog = list(map(int, progTxt.split(',')))
regCopy = deepcopy(reg)


for A in range(8**2, 8 ** 10):
    # print(A, end=' ')
    reg = deepcopy(regCopy)
    reg[0] = A
    out = run(prog, reg)
    if out[0] == 2 and out[1] == 4:
        print(A)

# A = 35184372115252
# reg[0] = A
# out = run(prog, reg)
# print(out)
