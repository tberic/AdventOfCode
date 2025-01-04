from copy import deepcopy

def combo(x):
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
            reg[0] = reg[0] // (2 ** combo(operand))
        elif op == 1:
            reg[1] = reg[1] ^ operand
        elif op == 2:
            reg[1] = combo(operand) % 8
        elif op == 3:
            if reg[0] != 0:
                index = operand
                continue
        elif op == 4:
            reg[1] = reg[1] ^ reg[2]
        elif op == 5:
            out = combo(operand) % 8
            if out != prog[len(output)]:
                return False
            output.append(out)
        elif op == 6:
            reg[1] = reg[0] // (2 ** combo(operand))
        elif op == 7:
            reg[2] = reg[0] // (2 ** combo(operand))

        index += 2
    
    return True


f = open('input.txt')

lines = [line.strip() for line in f]
reg = [0, 0, 0]
for i in range(3):
    _, regTxt = lines[i].split(': ')
    reg[i] = int(regTxt)

_, progTxt = lines[4].split(': ')
prog = list(map(int, progTxt.split(',')))
regCopy = deepcopy(reg)

# A = 8 ** 15
# A = 0b111100010001001001101000011001100000000000000000
# A = 0b111100010001001001101000011110010000000000000000
A = 0b111100010001001001101000011110110000001110011011 # the solution
while A < 8 ** 16:
    print(A)
    reg = deepcopy(regCopy)
    reg[0] = A
    if run(prog, reg):
        break
    A += 1

print(A)