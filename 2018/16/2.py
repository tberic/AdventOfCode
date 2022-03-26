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

commands = ["addr", "addi", 
            "mulr", "muli", 
            "banr", "bani", 
            "borr", "bori", 
            "setr", "seti", 
            "gtir", "gtri", "gtrr", 
            "eqir", "eqri", "eqrr"]

possible = {}
for i in range(16):
    possible[i] = set(commands)

i = -4
while i < len(lines):
    i += 4
    if lines[i] == "":
        i += 2
        break

    before = list(map(int, lines[i][9:-1].split(',')))
    instr = list(map(int, lines[i+1].split()))
    after = list(map(int, lines[i+2][9:-1].split(',')))

    for c in commands:
        if eval(c)(instr[1], instr[2], before) != after[instr[3]]:
            possible[ instr[0] ].discard(c)

start = i

possibleComm = {}
for comm in commands:
    for x in range(16):
        if comm in possible[x]:
            if comm in possibleComm:
                possibleComm[comm].add(x)
            else:
                possibleComm[comm] = set([x])

used = {c: 0 for c in commands}
while True:
    done = True
    for comm in commands:
        if not used[comm] and len(possibleComm[comm]) == 1:
            x = list(possibleComm[comm])[0]
            c = comm
            done = False
            used[comm] = 1
            break            
    
    if done:
        break
            
    for comm in possibleComm:
        if comm != c and x in possibleComm[comm]:
            possibleComm[comm].discard(x)            


command = {}
for comm in possibleComm:
    command[list(possibleComm[comm])[0]] = comm


reg = [0, 0, 0, 0]
for i in range(start, len(lines)):
    instr, A, B, C = list(map(int, lines[i].split()))
    reg[C] = eval(command[instr])(A, B, reg)

print(reg)