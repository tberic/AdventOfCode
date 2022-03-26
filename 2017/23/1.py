f = open('input.txt', 'r')
lines = [line.strip() for line in f]
f.close()

reg = {}
for c in 'abcdefgh':
    reg[c] = 0

count = 0
i = 0
while 0 <= i < len(lines):
    instr, a, b = lines[i].split()

    #print(i, instr, a, b, reg)
    #input()

    if a[0] in '-0123456789':
        a = int(a)
        X = "a"
    else:
        X = "reg['"+a+"']"

    if b[0] in '-0123456789':
        b = int(b)
        Y = "b"
    else:
        Y = "reg['"+b+"']"

    if instr == "set":
        exec(X+"="+str(eval(Y)))        
    elif instr == "sub":
        exec(X+"-="+str(eval(Y)))
        #reg[eval(X)] -= eval(Y)
    elif instr == "mul":
        count += 1
        exec(X+"*="+str(eval(Y)))
        #reg[eval(X)] *= eval(Y)
    elif instr == "jnz":
        if eval(X) != 0:
                i += eval(Y)
                continue
    i += 1

print(count)