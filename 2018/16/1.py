def addr(A, B, reg):
    return reg[A] + reg[B]

def addi(A, B, reg):
    return reg[A] + B

def mulr(A, B, reg):
    return reg[A] * reg[B]

def muli(A, B, reg):
    return reg[A] * B

def banr(A, B, reg):
    return reg[A] & reg[B]

def bani(A, B, reg):
    return reg[A] & B

def borr(A, B, reg):
    return reg[A] | reg[B]

def bori(A, B, reg):
    return reg[A] | B

def setr(A, B, reg):
    return reg[A]

def seti(A, B, reg):
    return A

def gtir(A, B, reg):
    return A > reg[B]

def gtri(A, B, reg):
    return reg[A] > B

def gtrr(A, B, reg):
    return reg[A] > reg[B]

def eqir(A, B, reg):
    return A == reg[B]

def eqri(A, B, reg):
    return reg[A] == B

def eqrr(A, B, reg):
    return reg[A] == reg[B]


f = open('input.txt', 'r')
lines = [line.strip() for line in f]
f.close()

s = 0
i = -4
while i < len(lines):
    i += 4
    if lines[i] == "":
        i += 2
        break

    before = list(map(int, lines[i][9:-1].split(',')))
    instr = list(map(int, lines[i+1].split()))
    after = list(map(int, lines[i+2][9:-1].split(',')))

    #print(before, instr, after)

    # if anything except the C reg is not equal before and after, continue
    # check if registers are within range

    count = 0
    if addr(instr[1], instr[2], before) == after[instr[3]]:
        count += 1
    if addi(instr[1], instr[2], before) == after[instr[3]]:
        count += 1
    if mulr(instr[1], instr[2], before) == after[instr[3]]:
        count += 1
    if muli(instr[1], instr[2], before) == after[instr[3]]:
        count += 1
    if banr(instr[1], instr[2], before) == after[instr[3]]:
        count += 1
    if bani(instr[1], instr[2], before) == after[instr[3]]:
        count += 1
    if borr(instr[1], instr[2], before) == after[instr[3]]:
        count += 1
    if bori(instr[1], instr[2], before) == after[instr[3]]:
        count += 1
    if setr(instr[1], instr[2], before) == after[instr[3]]:
        count += 1
    if seti(instr[1], instr[2], before) == after[instr[3]]:
        count += 1
    if gtir(instr[1], instr[2], before) == after[instr[3]]:
        count += 1
    if gtri(instr[1], instr[2], before) == after[instr[3]]:
        count += 1
    if gtrr(instr[1], instr[2], before) == after[instr[3]]:
        count += 1
    if eqir(instr[1], instr[2], before) == after[instr[3]]:
        count += 1
    if eqri(instr[1], instr[2], before) == after[instr[3]]:
        count += 1
    if eqrr(instr[1], instr[2], before) == after[instr[3]]:
        count += 1

    if count >= 3:
        s += 1

print(s)

#print(lines[i])
# for j in range(i, len(lines)):
#     print(lines[j])