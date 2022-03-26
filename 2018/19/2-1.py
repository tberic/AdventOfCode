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
    return int(A > reg[B])

def gtri(A, B, reg):
    return int(reg[A] > B)

def gtrr(A, B, reg):
    return int(reg[A] > reg[B])

def eqir(A, B, reg):
    return int(A == reg[B])

def eqri(A, B, reg):
    return int(reg[A] == B)

def eqrr(A, B, reg):
    return int(reg[A] == reg[B])

def reg(c):
    return chr( ord('a')+int(c) )


f = open('input.txt', 'r')
g = open('output.txt', 'w')
lines = [line.strip() for line in f]
for line in lines[1:]:
    instr, A, B, C = line.split()

    if instr == "addr":
        print(reg(C) + '=' + reg(A) + '+' + reg(B), file=g)
    elif instr == "addi":
        print(reg(C) + '=' + reg(A) + '+' + B, file=g)
    elif instr == "mulr":
        print(reg(C) + '=' + reg(A) + '*' + reg(B), file=g)
    elif instr == "muli":
        print(reg(C) + '=' + reg(A) + '*' + B, file=g)
    elif instr == "banr":
        print(reg(C) + '=' + reg(A) + '&' + reg(B), file=g)
    elif instr == "bani":
        print(reg(C) + '=' + reg(A) + '&' + B, file=g)
    elif instr == "borr":
        print(reg(C) + '=' + reg(A) + '|' + reg(B), file=g)
    elif instr == "bori":
        print(reg(C) + '=' + reg(A) + '|' + B, file=g)
    elif instr == "setr":
        print(reg(C) + '=' + reg(A), file=g)
    elif instr == "seti":
        print(reg(C) + '=' + A, file=g)
    elif instr == "gtir":
        print(reg(C) + '=' + A + '>' + reg(B), file=g)
    elif instr == "gtri":
        print(reg(C) + '=' + reg(A) + '>' + B, file=g)
    elif instr == "gtrr":
        print(reg(C) + '=' + reg(A) + '>' + reg(B), file=g)
    elif instr == "eqir":
        print(reg(C) + '=' + A + '==' + reg(B), file=g)
    elif instr == "eqri":
        print(reg(C) + '=' + reg(A) + '==' + B, file=g)
    elif instr == "eqrr":
        print(reg(C) + '=' + reg(A) + '==' + reg(B), file=g)

g.close()
f.close()
