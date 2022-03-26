def spin(n):
    global s
    s = s[-n:] + s[:-n]

def exchange(i, j):
    global s
    t = list(s)
    c = t[i]
    t[i] = t[j]
    t[j] = c
    s = "".join(t)

def partner(a, b):
    global s
    exchange(s.find(a), s.find(b))


f = open('input.txt', 'r')
line = f.readline().strip()
f.close()

s = "".join([chr(i) for i in range(97, 113)])

for instr in line.split(','):
    if instr[0] == "s":
        spin( int(instr[1:]) )
    elif instr[0] == "x":
        w = instr[1:].split('/')
        exchange( int(w[0]), int(w[1]) )
    elif instr[0] == "p":
        w = instr[1:].split('/')
        partner( w[0], w[1] )

print(s)