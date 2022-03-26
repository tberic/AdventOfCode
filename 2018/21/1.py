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

a = 6973579 # too low
a = 0
reg = [a, 0, 0, 0, 0, 0]

seen = set()
last = 0
i = 0
while 0 <= i < len(lines):
    instr, A, B, C = lines[reg[ip]].split()

    reg[int(C)] = eval(instr)(int(A), int(B), reg)

    if reg[ip] == 28:
        print(last)
        if reg[5] in seen:
            print('And then it repeats')
            break
        seen.add(reg[5])
        last = reg[5]

    reg[ip] += 1