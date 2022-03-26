def solve(n):
    global prog
    i = 0
    val = { 'x': 0, 'y': 0, 'z': 0, 'w': 0 }
    for line in prog:
        if line[:3] == "inp":
            op, b = line.split()
            val[b] = int(str(n)[i])
            i += 1
            #print('-'*10 + 'INPUT' + '-'*10)
        else:
            op, a, strb = line.split()
            if strb[0] in '0123456789-':
                b = int(strb)
            else:
                b = val[strb]

            if op == "add":
                val[a] = val[a] + b
            elif op == "mul":
                val[a] = val[a] * b
            elif op == "div":
                val[a] = val[a] // b
            elif op == "mod":
                val[a] = val[a] % b
            elif op == "eql":
                val[a] = int(val[a]==b)
        #print(val)
    return val["z"]

f = open('input.txt', 'r')

prog = [line.strip() for line in f]

n = 99999999999999
print(solve(n))
# while solve(n):
#     print(n)
#     n -= 1
#print(n)

f.close()