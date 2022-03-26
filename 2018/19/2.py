def reg(c):
    return chr( ord('a')+int(c) )

def translate(s):
    instr, A, B, C = s.split()

    if instr == "addr":
        return reg(C) + '=' + reg(A) + '+' + reg(B)
    elif instr == "addi":
        return reg(C) + '=' + reg(A) + '+' + B
    elif instr == "mulr":
        return reg(C) + '=' + reg(A) + '*' + reg(B)
    elif instr == "muli":
        return reg(C) + '=' + reg(A) + '*' + B
    elif instr == "banr":
        return reg(C) + '=' + reg(A) + '&' + reg(B)
    elif instr == "bani":
        return reg(C) + '=' + reg(A) + '&' + B
    elif instr == "borr":
        return reg(C) + '=' + reg(A) + '|' + reg(B)
    elif instr == "bori":
        return reg(C) + '=' + reg(A) + '|' + B
    elif instr == "setr":
        return reg(C) + '=' + reg(A)
    elif instr == "seti":
        return reg(C) + '=' + A
    elif instr == "gtir":
        return reg(C) + '=' + A + '>' + reg(B)
    elif instr == "gtri":
        return reg(C) + '=' + reg(A) + '>' + B
    elif instr == "gtrr":
        return reg(C) + '=' + reg(A) + '>' + reg(B)
    elif instr == "eqir":
        return reg(C) + '=' + A + '==' + reg(B)
    elif instr == "eqri":
        return reg(C) + '=' + reg(A) + '==' + B
    elif instr == "eqrr":
        return reg(C) + '=' + reg(A) + '==' + reg(B)
    

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

regi = [1, 0, 0, 0, 0, 0]

while 0 <= regi[ip] < len(lines):
    print(regi[ip], translate(lines[regi[ip]]), regi)
    instr, A, B, C = lines[regi[ip]].split()

    regi[int(C)] = eval(instr)(int(A), int(B), regi)

    regi[ip] += 1
    input()


print(regi[0])