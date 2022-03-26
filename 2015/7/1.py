import re

val = {}

def eval(s):
    global eq

    if s in val:
        return val[s]

    #print s
    if s[0] in '0123456789':
        val[s] = int(s)
        return int(s)
    else:
        val[s] = parse(eq[s])
        return val[s]

def parse( l ):
    global eq
    a, op, b = l
    print(l)
    if op == "":
        return eval(a)
    elif op == "NOT":
        return ~eval(b)
    elif op == "AND":
        return eval(a) & eval(b)
    elif op == "OR":
        return eval(a) | eval(b)
    elif op == "LSHIFT":
        return eval(a) << eval(b)
    elif op == "RSHIFT":
        return eval(a) >> eval(b)
    return None

f = open('input.txt', 'r')

eq = {}

for line in f:    
    l, res = line.split(' -> ')
    res = res.strip()
    if len(l.split()) == 3:
        a, op, b = l.split()
    elif len(l.split()) == 2:
        op, b = l.split()
        a = ""
    else:
        a = l.split()[0]
        op = ""
        b = ""
    eq[res] = [a, op, b]

print(eq['a'])

# for x, y in eq.items():
#     print(x, y)

print(parse(eq['a']))

f.close()