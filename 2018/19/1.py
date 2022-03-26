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


f = open('input.txt', 'r')
lines = [line.strip() for line in f]
ip = int(lines.pop(0)[-1])
f.close()

reg = [0, 0, 0, 0, 0, 0]

while 0 <= reg[ip] < len(lines):
    # print(reg[ip], lines[reg[ip]], reg)
    instr, A, B, C = lines[reg[ip]].split()

    reg[int(C)] = eval(instr)(int(A), int(B), reg)

    reg[ip] += 1


print(reg[0])